from django.core.management.base import BaseCommand
from django.core.files import File
from io import BytesIO
from product.models import ProductType, Category, Product, Variant, VariantValue, ProductImage, ProductSpecification
from django.utils.text import slugify
from django.db import transaction
from lorem_text import lorem
import random
from faker import Faker
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates African cultural products with enhanced variety'

    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, nargs='?', default=300,
                            help='Number of products to create')

    @transaction.atomic
    def handle(self, *args, **options):
        num_products = options['num_products']
        User = get_user_model()
        # Ensure User exists
        admin_user = User.objects.get(pk=1)  # Adjust this if the default ID is different

        # Ensure Product Type exists
        art_type, _ = ProductType.objects.get_or_create(
            name="African Cultural Heritage",
            defaults={'description': "Authentic cultural artifacts and traditional items from various African communities"}
        )

        # Expanded Cultural Categories
        cultural_categories = [
            "Tribal Masks", "Bronze Castings", "Beadwork", "Pottery",
            "Textiles & Weaving", "Wood Carvings", "Musical Instruments",
            "Ceremonial Objects", "Body Adornments", "Basketry",
            "Storytelling Artifacts", "Royal Regalia", "Traditional Jewelry",
            "Ancestral Figures", "Initiation Ceremony Items", "Dance Costumes",
            "Ritual Objects", "Household Implements", "Warrior Artifacts",
            "Divination Tools"
        ]

        # Create categories with tree structure
        root = Category.objects.create(name="African Cultural Arts")
        category_objects = [root]

        for cat_name in cultural_categories:
            category = Category.objects.create(
                name=cat_name,
                parent=root
            )
            category_objects.append(category)

        # Enhanced Cultural Variants
        variants_data = [
            ("Origin", ["Yoruba", "Zulu", "Maasai", "Ashanti", "Bamileke", "Tuareg", "Hausa", "San"]),
            ("Material", ["Sacred Wood", "Raffia", "Bronze", "Beads", "Clay", "Ivory", "Cowrie Shells", "Iron"]),
            ("Age", ["Contemporary", "Vintage (20-50 yrs)", "Antique (50+ yrs)", "Ancient"]),
            ("Usage", ["Ritual", "Daily Use", "Ceremonial", "Decorative", "Spiritual"]),
            ("Technique", ["Lost-wax Casting", "Hand-carved", "Hand-woven", "Batik", "Embroidery"])
        ]

        # Create variants and values
        variant_value_objects = {}
        for var_name, values in variants_data:
            variant, _ = Variant.objects.get_or_create(
                name=var_name,
                product_type=art_type
            )
            variant_value_objects[var_name] = []
            for value in values:
                vv, _ = VariantValue.objects.get_or_create(
                    variant=variant,
                    value=value
                )
                variant_value_objects[var_name].append(vv)

        # Cultural artifact names and descriptions
        cultural_terms = [
            "Ancestral", "Sacred", "Ritual", "Ceremonial", "Tribal",
            "Initiation", "Royal", "Spiritual", "Mythological", "Cosmological"
        ]

        fake = Faker()

        for i in range(num_products):
            # Generate culturally relevant name
            product_name = (
                f"{random.choice(cultural_terms)} {fake.unique.word().title()} "
                f"from the {random.choice(variant_value_objects['Origin'])} People"
            )

            product = Product.objects.create(
                name=product_name,
                description=lorem.paragraphs(3),
                price=random.uniform(500, 10000),
                history=lorem.paragraph(),
                category=random.choice(category_objects),
                user=admin_user,
                product_type=art_type,
            )

            # Add multiple images with cultural context
            for img_num in range(random.randint(1, 4)):
                is_primary = img_num == 0
                # Create a BytesIO object to hold the image data
                image_data = BytesIO(fake.image(image_format='JPEG'))

                # Create a File object using the BytesIO object
                ProductImage.objects.create(
                    product=product,
                    image=File(image_data, name=f'{slugify(product_name)}_{img_num}.jpg'),
                    is_primary=is_primary,
                    alt_text=f"{product_name} - {['Detail', 'Context View', 'Craftsperson'][img_num % 3]}"
                )
            # Add rich specifications
            for var_name in variant_value_objects:
                if random.random() > 0.3:  # 70% chance to add each spec
                    ProductSpecification.objects.create(
                        product=product,
                        name=var_name,
                        value=random.choice(variant_value_objects[var_name]).value
                    )

        self.stdout.write(self.style.SUCCESS(f"Created {num_products} cultural products."))
