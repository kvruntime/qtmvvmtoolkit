# coding:utf-8


import typing

# public class IntToBoolConverter : IValueConverter
# {
#     public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
#     {
#         return (int)value != 0;
#     }

#     public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
#     {
#         return (bool)value ? 1 : 0;
#     }
# }


class IValueConverter(typing.Protocol):
    source_type: type
    target_type: type

    def __init__(self, source_type: type, target_type: type) -> None: ...

    def convert(
        self, value: object, parameter: typing.Optional[object] = None
    ) -> object: ...

    def convert_back(
        self, value: object, parameter: typing.Optional[object] = None
    ) -> object: ...


class ToStrConverter(IValueConverter):
    def __init__(self, source_type: type, target_type: type) -> None:
        super().__init__(source_type, target_type)
        self.source_type = source_type
        self.target_type = target_type
        return

    def convert(
        self, value: object, parameter: typing.Optional[object] = None
    ) -> object:
        print("converter-->")
        return f"{value}%"

    def convert_back(
        self, value: object, parameter: typing.Optional[object] = None
    ) -> object:
        return str(value).capitalize()


class IConverter:
    def __init__(self) -> None:
        pass

    def convert(
        self,
        targetType: type,
        value: object | None = None,
        parameter: object | None = None,
    ) -> None: ...
