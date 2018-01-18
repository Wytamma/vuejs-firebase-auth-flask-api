from zappa.async import task
from core.logging import logger
from gmail import GMail, Message
from config._passwords import EMAIL_PASSWORD, EMAIL_ADDRESS


# Set up emailer
gmail = GMail(EMAIL_ADDRESS, EMAIL_PASSWORD)

@task
def email(email, subject, body, html=None):
    """ Sends email """
    logger.info(
        f'Sending email to {email}... '
        f'Subject: {subject}  '
        f'Body: {body}'
        )
    msg = Message(
        subject,
        to='%s <%s>' % (email, email),
        text=body,
        html=html
        )

    gmail.send(msg)
