using lumora_backend.Data;
using lumora_backend.Services.UserService;
using lumora_backend.Services.AwsService;
using lumora_backend.Utils;
using Microsoft.EntityFrameworkCore;


var builder = WebApplication.CreateBuilder(args);
// Add services to the container.

// Get db Connection string
var connectionString = await UtilsHelper.BuildConnectionStringAsync(builder.Configuration, "lumora-dev-creds", "DefaultConnection");
// Console.WriteLine(connectionString);

// Add DB context with the resolved connection string
builder.Services.AddDbContext<DataContext>(options => options.UseSqlServer(connectionString));

// Register services (Like AutoMapper and other custom services)
builder.Services.AddAutoMapper(_ => { }, AppDomain.CurrentDomain.GetAssemblies()); // register all Automapper Profiles
builder.Services.AddScoped<IUserService, UserService>(); // Every time we use the IUserService interface, it will use an instance of UserService.
builder.Services.AddScoped<IAwsService, AwsService>(); // Every time we use the IUserService interface, it will use an instance of UserService.

// Configure CORS Policy
builder.Services.AddCors(p => p.AddPolicy("cors_policy", build =>
{
    // build.WithOrigins("*").AllowAnyMethod().AllowAnyHeader(); // Allow every website
    build.WithOrigins("http://localhost:3000").AllowAnyMethod()
        .AllowAnyHeader(); // Only allow request from one React client
}));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors("cors_policy");
app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();