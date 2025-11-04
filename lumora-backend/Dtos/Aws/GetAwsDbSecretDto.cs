using System.Text.Json.Serialization;

namespace lumora_backend.Dtos.Aws;

public class GetAwsDbSecretDto
{
    [JsonPropertyName("username")]
    public string Username { get; set; } = string.Empty;

    [JsonPropertyName("password")]
    public string Password { get; set; } = string.Empty;

    [JsonPropertyName("engine")]
    public string Engine { get; set; } = string.Empty;

    [JsonPropertyName("host")]
    public string Host { get; set; } = string.Empty;

    [JsonPropertyName("port")]
    public int Port { get; set; }

    [JsonPropertyName("dbInstanceIdentifier")]
    public string DbInstanceIdentifier { get; set; } = string.Empty;
}