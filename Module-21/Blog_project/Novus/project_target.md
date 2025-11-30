# Functionalities
- Category 
- Tag
- User
- Post
- Comment

-----------------------------------------------------------------
-----------------------------------------------------------------


# Relationships:

### 1️⃣ Category & Post
- 1 category can have Multiple Post
- 1 post can have 1 post
- **Category & Post == `1 to Many`**

### 2️⃣Tag & Post
- 1 post can have Multiple tags
- 1 tag can have Multiple Post
- **Post and Tag == `Many to Many`**

### 3️⃣User & Post
- 1 user can have multiple post
- 1 Post can have 1 User
- **User and Post == `1 to Many`**

### 4️⃣User & Comment
- 1 user can have 1/multiple Comment
- **User and Comment == `1 to Many`**

### 5️⃣Comment & Post
- 1 Post can have 1/multiple Comments
- 1 Comment can not be in multiple Posts
- **Comment and Post == `1 to Many`**


### 6️⃣User & Like
- 1 Post can have Multiple Likes
- 1 User can Like Multiple Posts
- **User & Like == `Many to Many`**


