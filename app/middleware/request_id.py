blacklisted = await redis.get(f"blacklist:{jti}")

if blacklisted:
    raise UnauthorizedException()