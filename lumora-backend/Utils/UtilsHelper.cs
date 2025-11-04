using lumora_backend.Services.AwsService;

namespace lumora_backend.Utils
{
    public static class UtilsHelper
    {
        /// Build a database connection string either from  a database secret hosted on AWS Secrets Manager
        /// or falls back to a local default connection string. Then return the Resolved connection string
        public static async Task<string> BuildConnectionStringAsync(IConfiguration configuration, string awsSecretName, string defaultConnectionName)
        {
            // Validation & create AwsService instance
            if (configuration == null) throw new ArgumentNullException(nameof(configuration));
            var awsService = new AwsService();

            try
            {
                // Build a connection String from aws secrets
                var connectionString = await awsService.GetConnectionStringFromAwsDbAsync(awsSecretName);

                // Check if the connection string is NOT empty
                if (!string.IsNullOrWhiteSpace(connectionString))
                {
                    Console.WriteLine("Using AWS DB connection string.");
                    return connectionString;
                }

                // teh connection string is empty
                throw new Exception("AWS secret returned empty connection string.");
            }
            catch (Exception ex)
            {
                // Fallback to the default connection string from appsettings.Development.json
                var fallbackConnection = configuration.GetConnectionString(defaultConnectionName)
                                         ?? throw new InvalidOperationException(
                                             $"Default connection '{defaultConnectionName}' is missing.");

                // Return fallback connection string
                Console.WriteLine($"Falling back to default DB connection string. Reason: {ex.Message}");
                return fallbackConnection;
            }
        }
    }
}