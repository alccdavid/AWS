from aws_scrapper import AwsRegistrator
from logs.aws_logger import awslogger
from utils.temp_mail import generate_mail  # noqa
from config import configs


def main(emails: list[str]) -> None:
  """
    Creates AwsRegistrator instances using a list of provided emails and passwords.

    Args:
        emails (list[str]): A list of email and password pairs in the format "email@example.com:password".

    Returns:
        None
    """
  try:
    for email in emails:
      email, password = email.split(':', 1)
      aws = AwsRegistrator(email, password)
      aws.register()
      awslogger.log_info(f"AWS instance created with email: {email}")
  except BaseException as e:
    awslogger.log_critical(f"\nError creating AWS instance: {e}\n")


if __name__ == '__main__':
  email_list = [
      # Replace this with your list of emails and passwords
      "user1@example.com:password123",
      "user2@example.com:password456",
      "user3@example.com:password789",
  ]
  main(email_list)
