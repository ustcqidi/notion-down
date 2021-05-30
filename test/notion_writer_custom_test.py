import os
import unittest

from config import Config
from notion_reader import NotionReader
from notion_writer import NotionWriter
from utils.utils import Utils


class NotionWriterCustomConfigTest(unittest.TestCase):

    def test_write_posts_with_channel(self):
        Config.load_env()
        Config.set_debuggable(True)
        Config.set_blog_url("https://www.notion.so/kaedea/Noton-Down-Sample-440de7dca89840b6b3bab13d2aa92a34")
        Config.set_output(os.path.join(Utils.get_workspace(), "build"))
        Config.set_channels(['GitHub'])

        NotionWriter.clean_output()

        notion_pages = NotionReader.handle_post()
        self.assertIsNotNone(notion_pages)
        for notion_page in notion_pages:
            notion_page.is_published()
            notion_page.get_title()
            notion_page.get_date()
            notion_page.get_category()
            notion_page.get_tag()
            notion_page.get_file_dir()
            notion_page.get_file_name()

            NotionWriter.handle_page(notion_page)
            pass

    def test_write_markdown_test_page_with_channel(self):
        Config.load_env()
        Config.set_debuggable(True)
        Config.set_blog_url("https://www.notion.so/kaedea/Noton-Down-Sample-440de7dca89840b6b3bab13d2aa92a34")
        Config.set_output(os.path.join(Utils.get_workspace(), "build"))
        Config.set_channels(['GitHub'])

        NotionWriter.clean_output()

        main_page = NotionReader.read_main_page()
        self.assertIsNotNone(main_page)

        test_page = Utils.find_one(main_page.children, lambda it: it and str(it.title) == "MarkDown Test Page")
        self.assertIsNotNone(test_page)

        md_page = NotionReader.handle_single_page(test_page)
        self.assertIsNotNone(md_page)

        NotionWriter.handle_page(md_page)
        pass

    def test_write_markdown_test_page_with_channels(self):
        Config.load_env()
        Config.set_debuggable(True)
        Config.set_blog_url("https://www.notion.so/kaedea/Noton-Down-Sample-440de7dca89840b6b3bab13d2aa92a34")
        Config.set_output(os.path.join(Utils.get_workspace(), "build"))
        Config.set_channels(['default', 'GitHub'])

        NotionWriter.clean_output()

        main_page = NotionReader.read_main_page()
        self.assertIsNotNone(main_page)

        test_page = Utils.find_one(main_page.children, lambda it: it and str(it.title) == "MarkDown Test Page")
        self.assertIsNotNone(test_page)

        md_page = NotionReader.handle_single_page(test_page)
        self.assertIsNotNone(md_page)

        NotionWriter.handle_page(md_page)
        pass

