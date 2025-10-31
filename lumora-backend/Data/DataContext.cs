using lumora_backend.Models;
using Microsoft.EntityFrameworkCore;

namespace lumora_backend.Data;

public class DataContext : DbContext
{
    // Constructor
    public DataContext(DbContextOptions<DataContext> options) : base(options) { }
    // These DbSet properties are used by EF Core to map tables to classes
    public DbSet<User> Users { get; set; }
    public DbSet<Subscription> Subscriptions { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        // One-to-one: User <-> Subscription
        modelBuilder.Entity<User>()
            .HasOne(u => u.MySubscription)
            .WithOne(s => s.MyUser)
            .HasForeignKey<Subscription>(s => s.UserId)
            .OnDelete(DeleteBehavior.Cascade); // optional: delete subscription if user deleted
    }

}