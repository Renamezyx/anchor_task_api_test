import time

from utils.json_tools import JSONFileHandler


class AccountManager:

    def __init__(self):
        self.json_tools = JSONFileHandler("account.json")

    def get_account(self, tags: list = None, region: str = None, user_id: int = None, strict_mode=True):
        accounts = self.json_tools.read("account")
        if strict_mode:
            accounts = {key: value for key, value in accounts.items() if value["state"] == 0}
        if user_id:
            account = accounts.get(str(user_id))
            if account and strict_mode:
                self.occupy_account(user_id)
            return account
        filtered_accounts = {}
        for key, account in accounts.items():
            if region and account["region"] != region:
                continue
            if tags and not all(tag in account["tag"] for tag in tags):
                continue
            filtered_accounts[key] = account

        if filtered_accounts:
            first_account = next(iter(filtered_accounts.values()))
            if strict_mode:
                self.occupy_account(first_account["user_id"])
            return first_account
        return None

    def occupy_account(self, user_id):
        self._manage_state(user_id, 1)

    def release_account(self, user_id):
        self._manage_state(user_id, 0)

    def _manage_state(self, user_id: int, state: int):
        accounts = self.json_tools.read("account")
        accounts[str(user_id)]["state"] = state
        self.json_tools.write("account", accounts)

    def _init_account(self):
        accounts = self.json_tools.read("account")
        for account in accounts.values():
            account["state"] = 0
        self.json_tools.write("account", accounts)


if __name__ == '__main__':
    account_manager = AccountManager()
    print(account_manager.get_account())
    account_manager._init_account()
