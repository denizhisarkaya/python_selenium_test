import time
import pytest

# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPositiveScenarious:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        # open browser
        driver = webdriver.Chrome()
        time.sleep(3)

        # go to webpage (Open page)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Puch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class = 'btn']")
        submit_button_locator.click()  # bu adımı yorum satırına alınca otomatikmen 32. satırda hata alıyoruz
        # çünkü click yapmadığı için kodda bi sonraki sayfaya geçemiyoruz.
        time.sleep(2)

        # Verify new page URL contains https://practicetestautomation.com/logged-in-successfully/
        # current = mevcut olan, geçerli
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"  # bu adımı yorum satırına alırsak
        # otomatikmen 36. satırda hata vericek çünkü url'ye doğru geçemediği için text'i bulamayacak

        # Verify new page contains expected text ("Congratulations" or "successfully logged in")
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"
        # bu üçünü kapatınca da 42. satır çalışmaz çünkü url'i gene bulamıcak.

        # Verify button log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button_locator.is_displayed()


# ini uzantılı dosyanın amacı markerlarımızı kaydetmek açıklamasını yapmak ve başka birisi projemizde çalıştığında ne olduğunu anlaması için