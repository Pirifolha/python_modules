from functools import wraps
from time import perf_counter, sleep
from typing import Any, Callable


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 3:
                power = args[2]
            else:
                power = args[0]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char == " " for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    raise Exception("Spell failed")


if __name__ == "__main__":
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retry spell...")
    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
