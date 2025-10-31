using lumora_backend.Services.ResponseService;
using lumora_backend.Dtos.User;

namespace lumora_backend.Services.UserService;

public interface IUserService
{
    Task<ResponseService<GetUserDto>> AddUser(AddUserDto newUser);
}