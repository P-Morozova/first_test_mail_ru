from login_page import LoginPage
from main_page import MainPage
import pytest
from selenium import webdriver

def test_mail_ru(driver):

    login_first = "test.firstman"
    password_first = "t2n1xAxaVRP"
    email_first = "test.firstman@mail.ru"

    login_second = "test.secondman"
    password_second = "YOiURrjps71"
    email_second = "test.secondman@mail.ru"

    letter_theme = "Test theme"
    letter_text = "Test text"

    driver.get("https://mail.ru/")
    login_page1 = LoginPage(login_first, password_first)
    login_page1.do_login(driver)

    main_page = MainPage(email_second)

    main_page.send_letter(driver, letter_theme, letter_text)
    main_page.exit_from_account(driver)

    login_page2 = LoginPage(login_second, password_second)
    login_page2.do_login(driver)

    main_page2 = MainPage(email_first)
    sender_email, sender_theme = main_page2.check_letter_receive(driver)

    assert sender_email == email_first, "The sender of the received message does not match the sender of the sent message!"
    assert sender_theme == letter_theme, "The subject of the received email does not match the subject of the sent one!"



