query_for_db = [
    {
        'role': 'system', 'content': """
        사용자의 질문과 데이터베이스를 참고해서, 특히 부정형 질문을 긍정형 질문으로 바꾸어라.
        ex)"일제강점기 시대에 활동했던 작가 중에 이중섭이 아닌 다른 작가의 작품을 추천해 줘." >>> "김환섭의 작품을 추천해 줘.",
        "이중섭의 작품 중 황소가 아닌 다른 작품을 추천해 줘." >>> "춤추는 가족, 아버지와 두 아들 등을 추천해 줘."
        "
        """
    }
]