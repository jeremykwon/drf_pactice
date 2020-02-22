from rest_framework import permissions


# 작성자에 한해서 권한 부여
class CustomIsAuthorOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해서만 조회 가능
    # list 에 대한 인증
    def has_permission(self, request, view):
        # SAFE_METHODS : 변경하지 않는 요청들 GET, HEAD, OPTIONS 이다.
        # 보는건 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
    
    # 작성자에 한해서만 쓰기 가능
    # detail 에 대한 인증
    def has_object_permission(self, request, view, obj):
        '''
        is_staff, is_superuser 등을 사용 가능하다.
        '''
        # 슈퍼 유저는 all pass
        if request.user.is_superuser:
            return True

        # SAFE_METHODS : 변경하지 않는 요청들 GET, HEAD, OPTIONS 이다.
        # 보는건 허용
        elif request.method in permissions.SAFE_METHODS:
            return True

        # 삭제는 슈퍼 유저만 가능
        if request.method == 'DELETE':
            return request.user.is_superuser
        
        # 수정 요청의 경우 작성자만 가능하도록
        return obj.author == request.user
