from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    Dict,
    Type,
    Union,
    Tuple,
)

P = ParamSpec("P")
R = TypeVar("R")

ExceptionMapping = Dict[Type[Exception], Union[Type[Exception], Exception]]


def convert_exceptions_to_api_compitable_ones(
    exception_to_api_exception: ExceptionMapping,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    
    exception_types_to_check: Tuple[Type[Exception], ...] = tuple(exception_to_api_exception.keys())

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            
            try:
                return func(*args, **kwargs)
            
            except Exception as e:
                
                api_exception_target = None
                
                for exc_type_in_mapping in exception_types_to_check:
                    if isinstance(e, exc_type_in_mapping):
                        api_exception_target = exception_to_api_exception[exc_type_in_mapping]
                        break 
                
                if api_exception_target is not None:
                    
                    if isinstance(api_exception_target, type) and issubclass(api_exception_target, Exception):
                        raise api_exception_target(*e.args) 
                    
                    else:
                        raise api_exception_target
                
                raise

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
        
    return decorator