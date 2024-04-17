from typing import ClassVar, List
import os
from os.path import join
from pydantic_settings import BaseSettings

BASE_DIR = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(BASE_DIR))

credit_cards = ["1234567890123456:123", "9876543210987654:456"]
for card in credit_cards:
  card_number, cvv = card.split(':')
  print("Card Number:", card_number)
  print("CVV:", cvv)

  class PrivateConfigs(BaseSettings):
    CVV: str = cvv
    CARD_NUMBER: str = card_number
    EXPIRE_DATE: str = "04/2026"
    CARDHOLDER: str = "BART LINDSAY"
    CAPTCHA_API_KEY: str = "dfa58fa843756b75b0ba1dd52fe60f6e"
    SIM_API_TOKEN: str = "7juULnMSNRK2eLf-wWt4882C-gqY9Ph4d-ytpEgs16-c3Fuynm61D95EAV"


class DirConfigs(BaseSettings):
  AWS_FILENAME: ClassVar[str] = "aws_data.json"
  CURRENT_SIM_INFO: ClassVar[str] = "current_sim.json"
  SRC_DIR: ClassVar[str] = os.path.dirname(BASE_DIR)
  DATA_DIR: ClassVar[str] = join(SRC_DIR, 'data')
  LOGS_DIR: ClassVar[str] = join(SRC_DIR, 'logs')
  LOG_FILE: ClassVar[str] = join(LOGS_DIR, 'aws_logs.log')
  LOG_CONFIG_FILE: ClassVar[str] = join(LOGS_DIR, 'logging.yaml')
  PATH_TO_SAVE: ClassVar[str] = os.path.join(DATA_DIR, AWS_FILENAME)
  PATH_OF_SIM_JSON: ClassVar[str] = os.path.join(DATA_DIR, CURRENT_SIM_INFO)


class AwsSettings(BaseSettings):
  MANDATORY_FIELDS: ClassVar[List[str]] = ['cards', 'emails', 'phones']
  REQUIRED_FIELDS: ClassVar[List[str]] = [
      'first_name', 'last_name', 'card_number', 'valid_date', 'cvv',
      'cardholder', "phone", 'full_name', 'email', 'root_pass', 'account_name',
      'verify_email_code', "city", "postal_code", "country", "full_address",
      "card"
  ]
  URL: ClassVar[
      str] = "https://portal.aws.amazon.com/billing/signup#/identityverification"
  ONLINE_COUNTRY_CODE: ClassVar[str] = '46'
  ONLINE_SIM_SERVICE: ClassVar[str] = 'Amazon'
  PHONE_LIMIT: ClassVar[int] = 9
  CARD_LIMIT: ClassVar[int] = 9
  EMAIL_LIMIT: ClassVar[int] = 9


class SubSettings(BaseSettings):
  sub_field: str | None = None


class Config(BaseSettings):
  sub_settings: SubSettings = SubSettings()
  private_configs: PrivateConfigs = PrivateConfigs()
  aws_configs: AwsSettings = AwsSettings()
  dir_configs: DirConfigs = DirConfigs()


configs = Config()

# Accepting list of credit card numbers and CVVs
