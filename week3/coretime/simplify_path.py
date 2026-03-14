class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        

        
        
        # stack 에 빈배열 생성
        # '/' 기준으로 문자열을 나눈다
        # 앞에 기본적으로 / 시작 뒤에 문자열이 없는경우 '/'삭제
        # '/' 뒤에 '/'가 더붙는다면 '/' 하나로 변환
        # '/' 뒤에'..'이 두개라면 '/'기준으로 앞에 문자열을 삭제
        # '..'일 경우 문자열이 없을때 '/' 빼고 다 삭제 
        # '...' 일 경우 문자열로 인식





        # 1. stack 생성
        stack = []
        # 2. path를 '/' 기준으로 split
        path
        # 3. split한 각 조각을 하나씩 확인
        # 4. 경우 나누기
        #    - '' 이면 무시
        #    - '.' 이면 무시
        #    - '..' 이면 stack이 비어있지 않을 때 pop
        #    - 그 외는 정상 폴더 이름이므로 stack에 append
        # 5. 마지막에 '/' + '/'.join(stack) 반환
        #    - stack이 비어있으면 '/'



        # 앞뒤에 동시에 문자열이 존재하지않으면 '/' pop
        # 연속된 '//'는 '/'로 변환
        # '.'가 2개일때는 앞에오는 '문자열','/' 삭제
        # '/','.','.','/' 일때 루트디렉토리보다 위로 올라가는것은 불가능 
        # '.'가 3개 이상일때는 유효한 디렉토리 경로로 확인
        
        # TODO: stack 빈 리스트 만들기

        # TODO: path를 '/' 기준으로 나누기

        # TODO: 나눈 경로들을 하나씩 확인하기
        # TODO: 현재 값이 '' 이거나 '.' 이면 건너뛰기
        # TODO: 현재 값이 '..' 이면
        # TODO: stack에 값이 있을 때만 pop() 하기
        # TODO: 그 외의 경우
        # TODO: stack에 현재 디렉터리명 추가하기

        # TODO: stack이 비어 있으면 '/' 반환하기

        # TODO: 비어 있지 않으면 '/' + '/'.join(stack) 반환하기
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)