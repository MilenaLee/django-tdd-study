from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_dir = r"C:\Users\USER\Desktop\django\django-tdd-study\chromedriver.exe"

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver_dir)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 미현이는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다
        self.browser.get(self.live_server_url)

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('작업 목록 시작', header_text)

        # 그녀는 바로 작업을 추가하리고 한다
        inputbox = self.browser.find_element_by_id("id_new_item")

        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "작업 아이템 입력"
        )

        # "방탄소년단 콘서트 가기"라고 텍스트 상자에 입력한다
        # (미현이는 아미이다ㅎㅎ)
        inputbox.send_keys("방탄소년단 콘서트 가기")

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 방탄소년단 콘서트 가기" 아이템이 추가된다
        inputbox.send_keys(Keys.ENTER)
        mihyun_list_url = self.browser.current_url
        self.assertRegex(mihyun_list_url, '/lists/.+')
        self.check_for_row_in_list_table("1: 방탄소년단 콘서트 가기")

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "방탄소년단 콘서트에서 굿즈 구입하기"라고 입력한다. (다시 말하지만 미현이는 아미이다!)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("방탄소년단 콘서트에서 굿즈 구입하기")
        inputbox.send_keys(Keys.ENTER)

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
        self.check_for_row_in_list_table("2: 방탄소년단 콘서트에서 굿즈 구입하기")
        self.check_for_row_in_list_table("1: 방탄소년단 콘서트 가기")

        # 새로운 사용자인 태형이가 사이트에 접속한다

        ## 새로운 브라우저 세션을 이용해서 미현이의 정보가
        ## 쿠키를 통해 유입되는 것을 방지한다
        self.browser.quit()
        self.browser = webdriver.Chrome(chromedriver_dir)

        # 태형이가 홈페이지에서 접속한다
        # 미현의 리스트는 보이지 않는다
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("방탄소년단 콘서트 가기", page_text)
        self.assertNotIn("방탄소년단 콘서트에서 굿즈 구입하기", page_text)

        # 태형이가 새로운 작업 아이템을 입력하기 시작한다.
        # 태형이는 아이돌이다ㅎㅎ
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("신곡 작업")
        inputbox.send_keys(Keys.ENTER)

        # 태형이가 전용 URL을 취득한다.
        v_list_url = self.browser.current_url
        self.assertRegex(v_list_url, '/lists/.+')
        self.assertNotEqual(v_list_url, mihyun_list_url)

        # 미현이가 입력한 흔적이 없다는 것을 다시 확인한다
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("방탄소년단 콘서트 가기", page_text)
        self.assertNotIn("방탄소년단 콘서트에서 굿즈 구입하기", page_text)

        # 둘 다 만족하고 잠자리에 든다

    def test_layout_and_styling(self):
        # 미현이는 메인 페이지를 방문한다
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 그녀는 입력 상자가 가운데 배치된 것을 본다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        inputbox.send_keys('testing\n')
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )