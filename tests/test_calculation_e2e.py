from playwright.sync_api import Page
import pytest


def test_addition_e2e(browser, base_url):
    page = browser.new_page()
    page.goto(base_url)
    response = page.evaluate(
        """
        () => fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operand1: 12, operand2: 3, operation: 'add' })
        }).then(res => res.json())
    """
    )
    assert response["result"] == 15


def test_divide_by_zero_e2e(browser, base_url):
    page = browser.new_page()
    page.goto(base_url)
    response = page.evaluate(
        """
        () => fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operand1: 10, operand2: 0, operation: 'divide' })
        }).then(res => {
            if (!res.ok) return res.json().then(e => { throw e.detail || JSON.stringify(e); });
            return res.json();
        }).catch(e => { return {error: e}; })
    """
    )
    assert "Division by zero" in response["error"]
