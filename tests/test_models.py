import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_get_articles(self):
        author = Author(1, "John Doe")
        # Mock or use a test database with known data
        articles = author.get_articles()
        self.assertIsInstance(articles, list)

    def test_author_get_magazines(self):
        author = Author(1, "John Doe")
        # Mock or use a test database with known data
        magazines = author.get_magazines()
        self.assertIsInstance(magazines, list)

    def test_article_save(self):
        article = Article(None, "Test Title", "Test Content", 1, 1)
        article.save()
        # Add assertions to verify the save operation

    def test_article_get_author(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        author = article.get_author()
        self.assertIsInstance(author, Author)

    def test_article_get_magazine(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        magazine = article.get_magazine()
        self.assertIsInstance(magazine, Magazine)

    def test_magazine_save_to_db(self):
        magazine = Magazine(None, "Tech Weekly", "Technology")
        magazine.save_to_db()
        # Add assertions to verify the save operation

    def test_magazine_get_articles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        articles = magazine.get_articles()
        self.assertIsInstance(articles, list)

    def test_magazine_get_contributors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        contributors = magazine.get_contributors()
        self.assertIsInstance(contributors, list)

    def test_magazine_get_article_titles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        titles = magazine.get_article_titles()
        self.assertIsInstance(titles, list)

    def test_magazine_get_frequent_contributors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        frequent_contributors = magazine.get_frequent_contributors()
        self.assertIsInstance(frequent_contributors, list)

    def test_author_id_type(self):
        author = Author(1, "John Doe")
        self.assertIsInstance(author.id, int)

    def test_article_content_length(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        truncated_content = "Test Content"[:30]
        self.assertEqual(article.content, truncated_content)

if __name__ == "__main__":
    unittest.main()
