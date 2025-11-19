import streamlit as st

# print("page reloaded")

# st.title("Hello Streamlit 👋")
# st.write("이건 Python으로 만든 웹 앱이에요!")
# st.write("그리고 nioptenv라는 가상환경에서 실행되고 있습니다.")
# name = st.text_input("이름을 입력하세요:")
# st.write(f"안녕하세요, {name}님!")

st.set_page_config(
    page_title = "포켓몬 도감",
    page_icon = "./images/pkm.png"
)

# Custom CSS 적용
st.markdown("""
<style>
h1 {
    color:red;
}

img {
     max-height: 300px;
}
 
.stVerticalBlock div {
    display: flex;
    justify-content: center;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# 예제)CSS Style    
# [data-testid="stIconMaterial"] {
#     visibility: hidden;
# }    

# .stExpander {
#     pointer-events: none;
# }


st.title("Hello Streamlit 👋")
# st.text("포켓몬을 하나씩 추가해서 도감을 채워보세요!")
# st.subheader("포켓몬을 하나씩 추가해서 도감을 채워보세요!")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

# 포켓몬 캐릭터 형태 emoji 및 아이콘
type_emoji_dict = {
    "노말" : "😁",
    "격투" : "🥷",
    "비행" : "🛩️",
    "독" : "🍄",
    "땅" : "🌋",
    "바위" : "🪨",
    "벌레" : "🐞",
    "고스트" : "👻",
    "불꽃" : "🔥",
    "물" : "💦",
    "풀" : "☘️",
    "전기" : "⚡",
    "에스퍼" : "👻",
    "얼음" : "🧊",
    "드래곤" : "🐉",
    "악" : "👿",
    "페어리" : "🦋",
    "강철" : "🚂"
}

# pokemon = {
#     "name": "누오",
#     "types": ["물", "땅"],
#     "image_url": "https://i.namu.wiki/i/gdSVPzHYUwSvgOFqxyjwQ-G6_PeRV8zD2BtzXBYPRRsgQeFhvqJhZn7ar8nwhN0FdxahK4ODzQTjn-_tHq1rouC_JcCCgeveZ7KugKj0kHxNz-TDcZU-vp7GwuPY16PVL4nuei2ckFR3j00Rniyh5Q.webp"
# }

# 포켓몬 캐릭터 리스트
initial_pokemons = [
    {
        "name": "피카추",
        "types": ["전기"],
        "image_url": "https://i.namu.wiki/i/vz2HsIOyWTkBCxN8GITi9IXR1oT0BjCl7x87GGm-nx7VX2dDn8v0LpmG1Swj3IhvS83-erlKN6EAO_CQ0r_wZMAOr9pqtd3QDFk4H79tTUu7Wo29A6o5mI14gYjZgND1tOrUHUDEc68BuG3lSFvu2w.webp"
    },    
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://i.namu.wiki/i/gdSVPzHYUwSvgOFqxyjwQ-G6_PeRV8zD2BtzXBYPRRsgQeFhvqJhZn7ar8nwhN0FdxahK4ODzQTjn-_tHq1rouC_JcCCgeveZ7KugKj0kHxNz-TDcZU-vp7GwuPY16PVL4nuei2ckFR3j00Rniyh5Q.webp"
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://i.namu.wiki/i/lAo1rV2hI3Hu-7WtdKWfxlpgrir83tzaZxbdNikKV7XIWNoBKIBlRIQqMh-0vhrOHrL4BAjS0d54IRozzYmG22xfa6o1h1ke2KiRiJkkww8ImeIxKaSfQHRURoR7Q8RDb1JZxRmsLWjY9DRtUBeNdQ.webp"
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://i.namu.wiki/i/qeBXi4XwoVkizDpuDHpWOU-mU6zVjvK0YXMR1jkvM__8K18owWVC86O8BEjcY5UhjR3cLx6TDayksqnbCW-XRt7S5Vp7AtueSheKihv4HPFSoimz0O9kMyx4YYugunZnDMxc4QBFmatFAuVtie8CBQ.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://i.namu.wiki/i/-q2MNn8TlPQ_3R8-2f2nP66RUsRLmllpL_nOWcEHYDb0T_WRvY08-EMcvh81czhcvkzmq2tyJMC5fAdG_zW9mBXv4XekSjjkisTscKbbzBZ5kZUg4uWYAFGADn9FxcFS6QDCfeJw6NBLDRgizjEPJQ.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://i.namu.wiki/i/-9cr1IN4odX5YEKSbs3CeZyjY5xGU7ghlMA2p5P2SwaUvsmOSgwRx2D-q8GjGjcfvVIM0v2szEBJdqKcv1Slrc_bFRy3q3YQZn6oIxDgABniHIfjpH0Sdi91mrThcAV_QUBv-S6jV3m7eD-W0k9Daw.webp"
    },    
]

# 예시 데이터
example_pokemon = {
        "name": "알로라 디그다",
        "types": ["땅", "강철"],
        "image_url": "https://i.namu.wiki/i/6dPAx3vvKjtXFB467VXz0Hm5kIsM3edKB2GGrltxb29girO55Ak10o0PNosKvkE1hiFkdbnNcSzM19RTz1Jvz3qCzjccfUOcTZR1Z9syf1SAB6u3SCla67IU7t-kcruoDDXi0gb_46p_5Iu4zhW3xQ.webp"
    }

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons
    
# Toggle을 이용한 Form 자동완성 기능
auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)

# Form에서 새로운 포켓몬을 추가
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:        
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="포켓몬 속성", 
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="포켓몬 이미지 URL",
        value=example_pokemon["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    
    # Submit 버튼 처리
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")            
            # st.session_state 저장공간에 딕셔너리 형태로 포켓몬을 저장 처리 함.
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                # Image URL이 없으면 Default URL(포켓몬볼)을 표시 처리
                "image_url": image_url if image_url else "https://i.namu.wiki/i/VgZ2Fjtb4U14pDBkWi7ozWOHe0XEUr39_6NCUjGXG27P33guy6g-3qp5KRllmzCIjDLHlCPE2O8DQeKk-ZAoG680ynEo6Ho1pFRbgf_9GHKF-SLLubWeF73JLDU1tVlSez_5vNQJ2KxECHJjlCgwNg.webp"
            })
            
            # session state(페이지가 살아있는 동안에 데이터를 저장하는 공간(dictionary)을 의미 함)

# 포켓몬 캐릭터 출력하기
for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                # st.subheader(pokemon["name"])
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                # st.subheader(" / ".join(emoji_types))    
                st.text(" / ".join(emoji_types))
                # Delete 처리
                delete_button = st.button(label="삭제", key=(i+j), use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    # 포켓몬을 삭제 처리 후 streamlit을 중단 함
                    # st.rerun() 코딩 여부 실행 순서
                    #  - 사용(X): page reloaded --> delete button
                    #  - 사용(O): delete button --> page reloaded                    
                    st.rerun()
                    