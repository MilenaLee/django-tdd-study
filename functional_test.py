from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

chromedriver_dir = r"C:\Users\USER\Desktop\django\django-tdd-study\chromedriver.exe"

class NewVisitorTest(unittest.TestCase):
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
        self.browser.get("http://localhost:8000")

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

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
        self.check_for_row_in_list_table("1: 방탄소년단 콘서트 가기")

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "방탄소년단 콘서트에서 굿즈 구입하기"라고 입력한다. (다시 말하지만 미현이는 아미이다!)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("방탄소년단 콘서트에서 굿즈 구입하기")
        inputbox.send_keys(Keys.ENTER)

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
        self.check_for_row_in_list_table("2: 방탄소년단 콘서트에서 굿즈 구입하기")
        self.check_for_row_in_list_table("1: 방탄소년단 콘서트 가기")

        # 미현이는 사이트가 입력한 목록을 잘 저장하는지 궁금하다
        # 사이트는 그녀를 위한 특정 url을 생성해준다
        # 이때 URL에 대한 설명도 함께 제공된다
        self.fail("Finish the test!")



if __name__ == "__main__":
    unittest.main(warnings="ignore")

