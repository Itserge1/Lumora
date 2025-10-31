using lumora_backend.Services.UserService;
using Microsoft.AspNetCore.Mvc;
using lumora_backend.Services.ResponseService;
using lumora_backend.Dtos.User;

namespace lumora_backend.Controllers;

[ApiController]
[Route("api/[controller]")]
public class UserController : ControllerBase
{
    private readonly IUserService _userService;
    private readonly ILogger _logger;

    public UserController(ILogger logger, IUserService userService)
    {
        _logger = logger;
        _userService = userService;
    }

    // TEST API
    [HttpGet("testApi")]
    public string TestApi()
    {
        return "Api is working!!";
    }

    [HttpPost("add")]
    public ActionResult<ResponseService<GetUserDto>> AddNewUser([FromBody] AddUserDto newUser)
    {
        return Ok(_userService.AddUser(newUser));
    }
}