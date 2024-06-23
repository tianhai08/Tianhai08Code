# simple_blog_system.py
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print(f"Title: {post.title}")
            print(f"Content: {post.content}")
            print()

if __name__ == "__main__":
    blog = Blog()
    post1 = Post("My First Post", "This is the content of my first post.")
    post2 = Post("Another Post", "Here is some more content.")
    blog.add_post(post1)
    blog.add_post(post2)
    blog.display_posts()
