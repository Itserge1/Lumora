using AutoMapper;
using lumora_backend.Dtos.User;
using lumora_backend.Models;

namespace lumora_backend;

public class AutoMapperProfile : Profile
{
    public AutoMapperProfile()
    {
        CreateMap<AddUserDto, User>();
        CreateMap<User, GetUserDto>();
    }
}