namespace lumora_backend.Services.AwsService;

public interface IAwsService
{
    Task<string> GetSecretAsync(string secretName, string region = "us-east-1");
}