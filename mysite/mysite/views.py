# 파이썬의 로깅 모듈을 임포트
import logging

# settings.py파일에서 설정된 로거를 취득함
logger = logging.getLogger('mylogger')


def my_view(result, arg1, arg):
    # 필요 로직
    if bad_mojo:
        # ERROR 레벨의 로그 레코드를 생성함
        logger.error('Something Went Wrong')
