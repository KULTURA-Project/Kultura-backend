from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates admin users'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # Get the custom user model

        # Create Admin User
        try:
            admin_user = User.objects.get(email="codewithbadolo@gmail.com")
            self.stdout.write(self.style.SUCCESS(f"Admin user already exists: {admin_user.email}"))
        except User.DoesNotExist:
            admin_user = User.objects.create_superuser(
                email="codewithbadolo@gmail.com",
                password="adminpassword123",
                first_name="Admin",
                last_name="User"
            )
            self.stdout.write(self.style.SUCCESS(f"Admin user created: {admin_user.email}"))
