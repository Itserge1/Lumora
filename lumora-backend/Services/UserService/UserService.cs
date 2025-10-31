using lumora_backend.Data;
using lumora_backend.Dtos.User;
using lumora_backend.Models;
using lumora_backend.Services.ResponseService;
using AutoMapper;
using Microsoft.EntityFrameworkCore;

namespace lumora_backend.Services.UserService;

public class UserService : IUserService
{
    private readonly DataContext _dataContext; // Database context (DI)
    private readonly IMapper _mapper;

    public UserService(DataContext dataContext, IMapper mapper)
    {
        this._dataContext = dataContext;
        this._mapper = mapper;
    }

    public async Task<ResponseService<GetUserDto>> AddUser(AddUserDto newUser)
    {
        // convert from Dto class to User class
        var myNewUser = _mapper.Map<User>(newUser);

        // Add user to DB (User id will be generated automatically base on the USEr model structure)
        _dataContext.Add(myNewUser);
        await _dataContext.SaveChangesAsync();

        // Get the newly added User info from Db (to store in a section later)
        User? newUserDb = _dataContext.Users.FirstOrDefault(u => u.Email!.ToLower() == newUser.Email!.ToLower());
        GetUserDto resUser = _mapper.Map<GetUserDto>(newUserDb);


        // Prepare response
        var myResponseService = new ResponseService<GetUserDto>()
        {
            Data = resUser,
            Success = true,
            Message = "Added User Successfully"
        };

        return myResponseService;
    }
}