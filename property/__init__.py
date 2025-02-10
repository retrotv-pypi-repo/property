"""
프로퍼티 관련 처리를 일관성 있게 하기 위한 프로퍼티 모듈
"""
import configparser
from configparser import SectionProxy


class Property(object):
    """
    프로퍼티 클래스
    """

    def __init__(self, filename: str, property_name: str) -> None:
        parser = configparser.ConfigParser()
        parser.read(filename)
        self.__properties = parser[property_name]

    @property
    def properties(self) -> SectionProxy:
        return self.__properties

    def get_value(self, key: str) -> str:
        try:
            return self.__properties[key]
        except KeyError:
            raise KeyError(f"{key} 이름을 가진 프로퍼티가 존재하지 않습니다.")
