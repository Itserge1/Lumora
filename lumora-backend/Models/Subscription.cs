using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace lumora_backend.Models;

public class Subscription
{
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int SubscriptionId { get; set; }

    [Required(ErrorMessage = "Subscription Name is required")]
    [MinLength(3, ErrorMessage = "Subscription Name must be at least 3 characters")]
    [MaxLength(50, ErrorMessage = "Subscription Name cannot be longer than 50 characters")]
    public string? Name { get; set; }

    [Required(ErrorMessage = "Description is required")]
    [MaxLength(200, ErrorMessage = "Description cannot be longer than 200 characters")]
    public string? Description { get; set; }

    [Required(ErrorMessage = "Price is required")]
    [Range(0, double.MaxValue, ErrorMessage = "Price must be 0 or greater")]
    public decimal Price { get; set; }

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    // Navigation Property
    [ForeignKey("User")]
    public int UserId { get; set; }
    public User? MyUser { get; set; }
}