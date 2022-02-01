from django.core.exceptions import ValidationError

def validate_title_content(value):
    if "#" in value:
        raise ValidationError('#은 들어갈 수 없어요.')

def validate_feeling(value):
    for i in value:
        if i.isdigit():
            raise ValidationError("숫자는 들어갈 수 없습니다")
    
def validate_score(value):
    if (value < 0) or (value > 10):
        raise ValidationError('숫자는 1부터 10 중애서만 입력해주세요')