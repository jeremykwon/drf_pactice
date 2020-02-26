from rest_framework.throttling import UserRateThrottle


# settings.py 에 정의되어 있다.
# ScopedRateThrottle 를 사용하므로 사용되지는 않는다. ( 코드가 조금 더 간단해지는 방법이 있으므로 )
class FirstCustomRateThrottle(UserRateThrottle):
    scope = 'custom'


class SecondCustomRateThrottle(UserRateThrottle):
    scope = 'custom2'


class UserCustomRateThrottle(UserRateThrottle):
    # 생성자에서 get_rate 가져오는 것이 불필요 하므로
    # 생성자 오버로딩을 통해 루틴 제거
    def __init__(self):
        pass

    def allow_request(self, request, view):
        premium_scope = getattr(view, 'premium_scope', None)
        light_scope = getattr(view, 'light_scope', None)
        
        # Profile 모델에 is_premium_user 필드가 있는 경우 ( 지정 필요 )
        if request.user.profile.is_premium_user:
            if not premium_scope:  # settings 에서 premium_scope 미지정 시에는 Throttling 제한을 하지 않음
                return True
            self.scope = premium_scope  # settings 에 정의된 scope

        else:
            if not light_scope:  # settings 에서 light_scope 미지정 시에는 Throttling 제한을 하지 않음
                return True
            self.scope = light_scope

        self.rate = self.get_rate()  # scope 값을 참조해서 실제 rate 값을 가져옴
        self.num_requests, self.duration = self.parse_rate(self.rate)  # 파싱
        
        # 값을 뽑아 부모에게 넘김
        return super().allow_request(request, view)
