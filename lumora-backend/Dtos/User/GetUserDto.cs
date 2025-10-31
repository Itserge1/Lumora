using System.ComponentModel.DataAnnotations;
using lumora_backend.Models;

namespace lumora_backend.Dtos.User;

public class GetUserDto
{
    public int UserId { get; set; }
    public string? Username { get; set; }
    public string? Email { get; set; }
    public string? Password { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    // Subscription Navigation Property: One-to-one relation with Subscription
    public Subscription? MySubscription { get; set; }
}