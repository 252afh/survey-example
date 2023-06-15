from django.test import TestCase

from pulse_survey.survey import models


class FeedbackModelTest(TestCase):
    def test_feedback_saved(self):
        feedback = models.Feedback(email="Test@Example.Com", content="Some feedback")
        feedback.save()
        self.assertEqual(feedback.content, "Some feedback")

    def test_email_saved_lowercase(self):
        feedback = models.Feedback(email="TeSt@ExAmPlE.CoM", content="Some feedback")
        feedback.save()
        self.assertEqual(feedback.email, "test@example.com")
