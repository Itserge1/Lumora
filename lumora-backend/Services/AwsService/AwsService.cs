using Amazon;
using Amazon.Runtime.CredentialManagement;
using Amazon.SecretsManager;
using Amazon.SecretsManager.Model;
using System.Text;
using lumora_backend.Dtos.Aws;
using System.Text.Json;

namespace lumora_backend.Services.AwsService;

public class AwsService : IAwsService
{
    private readonly IAmazonSecretsManager _awsSecretsManagerClient;
    public AwsService(string region = "us-east-1")
    {
        var regionEndpoint = RegionEndpoint.GetBySystemName(region);

        // Load AWS SSO Profile Credentials
        var chain = new CredentialProfileStoreChain();
        if (!chain.TryGetAWSCredentials("AdministratorAccess-318526443004", out var credentials))
        {
            throw new Exception($"AWS profile AdministratorAccess-318526443004 could not be found or loaded.");
        }

        _awsSecretsManagerClient = new AmazonSecretsManagerClient(credentials, regionEndpoint);
    }

    // AWS SECRETS
    public async Task<string> GetSecretAsync(string secretName, string region = "us-east-1")
    {
        if (string.IsNullOrWhiteSpace(secretName))
            throw new ArgumentException("Secret name cannot be null or empty.", nameof(secretName));

        var request = new GetSecretValueRequest
        {
            SecretId = secretName,
            VersionStage = "AWSCURRENT"
        };

        try
        {
            var response = await _awsSecretsManagerClient.GetSecretValueAsync(request);

            if (!string.IsNullOrEmpty(response.SecretString))
                return response.SecretString;

            if (response.SecretBinary != null)
                return Encoding.UTF8.GetString(response.SecretBinary.ToArray());

            throw new InvalidOperationException($"Secret '{secretName}' returned no value.");
        }
        catch (ResourceNotFoundException)
        {
            throw new KeyNotFoundException($"The requested secret '{secretName}' was not found.");
        }
    }

    public async Task<string> GetConnectionStringFromAwsDbAsync(string secretName)
    {
        // Check if the secret name is empty
        if (string.IsNullOrWhiteSpace(secretName))
            throw new ArgumentException("Secret name cannot be null or empty.", nameof(secretName));

        // Fetch secret from AWS
        var secretString = await GetSecretAsync(secretName);

        // Check if the secret value is empty
        if (string.IsNullOrWhiteSpace(secretString))
            throw new InvalidOperationException($"Secret '{secretName}' returned an empty value.");

        // Deserialize secret value into structured DTO safely
        var dbSecret = JsonSerializer.Deserialize<GetAwsDbSecretDto>(
            secretString,
            new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

        if (dbSecret == null)
            throw new InvalidOperationException($"Failed to deserialize secret '{secretName}'.");

        // Build and return a connection string 
        string connectionString = $"server={dbSecret.Host},{dbSecret.Port};Database={dbSecret.DbInstanceIdentifier};User Id={dbSecret.Username};Password={dbSecret.Password};MultipleActiveResultSets=true;TrustServerCertificate=true;";
        return connectionString;
    }

    // public async Task<T?> GetSecretAsync<T>(string secretName)
    // {
    //     var secretString = await GetSecretAsync(secretName);
    //     return JsonSerializer.Deserialize<T>(secretString);
    // }
}