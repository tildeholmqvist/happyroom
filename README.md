# HappyRoom 

#### _Please note that this website is for educational purposes and should not be treated like a real website._

HappyRoom is a B2C e-commerce store targeting individuals looking to enhance their living or working spaces with unique wallpapers and interior design services.

At HappyRoom, the users can explore a variety of carefully selected wallpapers, each with its own distinct design to suit different tastes.
The user are also offered personalized assistance through consultations with our team of experts.
Additionally, the user can stay informed about new arrivals and special offers by subscribing to our newsletter, and also share their thoughts with us through our customer reviews.

HappyRoom aims to provide users with the tools and resources needed to transform their spaces into personalized expressions of style and creativity. 

HappyRoom uses Stripe as a payment method.
Please note:
_You should not enter any personal credit or debit card information, since this store is only for educational purposes._

For a live demonstration, visit [HappyRoom](https://happy-room-e68715746875.herokuapp.com/)

![HappyRoom, screenshot from Am I responsive?](/docs/readme_images/happyroom.png)

## Table of Contents

## UX

### User Stories
##### Profile
- As a site user I can sign up to the site so that my own personal account is created.
- As a site user I can log in and log out of the page.
- As a logged i user I can choose if I want to save my information so that it will speed up the checkout process next time.
- As a site user I can buy products of the store while im logged in so that it's an easier process for me viewing my prefilled personal details.
- As a site user I can view my previously made orders so that I can easily find what I bought last time
- As a logged in user I can easily see that I am activily logged in so that if I am not, I can log in

##### Products

- As a site user I can easily navigate through the website so that I can find what I am looking for
- As a site user I can easily brows through the different products so that I can find what I am looking for.
- As a site user I can sort and filter the products so that I only view the product I am interested in.
- As a site user I can save or like products so that I can easily find them again.
- As a site user I can find inspirational images of the products so that i can imagine what the room will look like
- As a site user I can view my shopping bag and the total price so that I know how much money I shop for.
- As a site user I can be assured that the payment is secure.

##### Other requirements
- As a site user I can sign up for newsletter
- As a site user I can book a meeting with an expert so that I can get help with advising and design.
- As a site user I am informed about how my personal information is going to be handled, and what the stores privacy policy is.
- As a site user I can fast and easily find information about the company so that I can get answers if I have any questions

##### Site Administration
- As a site owner I can create, edit and delete products
- As a site owner I can send out newsletter so that the user who signed up for it can recieve them
- As a site owner I can inform the user about the company so that the user knows what the purpose of the company and site is

#### Future User Stories to Consider
- As a site user I can post images with my customer review
- As a site user I can find a gallery with pictures showing how expert advice helped previous customers.

## Design & Layout 
The site features a clean design with earthy elements, blending brown with white for a calm and luxurious atmosphere.

### Color Scheme 

The color scheme of HappyRoom is soothing, mainly in earthy tones. These colors harmonize well with the website's purpose, offering users a relaxed and welcoming environment.

The Color Scheme is made with [Color Space](https://mycolor.space/).

### Images
All media is uploaded with Amazon Web Services and all images is borrowed from the real wallpaper site 
[Belarte Studio.](https://belartestudio.com/)

_Please note that this website is for educational purposes only and should not be regarded as a real e-commerce platform. For genuine products, visit [Belarte Studio.](https://belartestudio.com/)_

### Logo

The logo of HappyRoom is made in [Canva](https://www.canva.com/sv_se/), and is written in the fonts Libre Baskerville and Brittany.

![Picture of the Logo](/docs/readme_images/logo-pic.png)


### Fonts

The Montserrat font is used on the main content of the website, for example, all product description and FAQ page. 
The Playfair Display font is used on all product headings. 
The Libre Baskerville is used on all other headings on the site.

All fonts are from [Google Fonts](https://fonts.google.com/).

### Favicon 

The favicon was generated through [Favicon.io](https://favicon.io/) and depicts a roll of wallpaper.

### Icons

All icons and symbols are from [Font Awesome.](https://fontawesome.com/)

### Wireframes

Wireframes were produced using Balsamiq.

<details>

 <summary>Home Page</summary>

![Home Page](docs/wireframes/home-page.png)
</details>

<details>

 <summary>Product Page</summary>

![Product Page](docs/wireframes/product-page.png)
</details>

<details>

 <summary>Product Detail Page</summary>

![Product Detail Page](docs/wireframes/product-detail.png)
</details>

<details>

 <summary>Service Page</summary>

![Service Page](docs/wireframes/service-page.png)
</details>

<details>

 <summary>Service Detail Page</summary>

![Service Detail Page](docs/wireframes/book-service-page.png)
</details>

<details>

 <summary>FAQ</summary>

![FAQ Page](docs/wireframes/FAQ.png)
</details>

<details>

 <summary>Customer Reviews</summary>

![Customer Reviews](docs/wireframes/customer-reviews.png)
</details>

<details>

 <summary>Product Management</summary>

![Product Management](docs/wireframes/product-management.png)
</details>

<details>

 <summary>Profile</summary>

![Profile](docs/wireframes/profile.png)
</details>

<details>

 <summary>Footer</summary>

![Footer](docs/wireframes/footer.png)
</details>
## Agile Methodology

For project management, I used GitHub Projects for an agile approach. You can access the project board [here.](https://github.com/users/tildeholmqvist/projects/10)

During the planning phase, I created twenty GitHub Issues, with two additional as future improvement.
Each issue is followed by a set of acceptance criteria, making the execution of the task clear, and easier to navigate to completion.

## Data Model

When building this B2C e-commerce site, the principles of object-oriented programming (OOP) was used, which organize data into easily manageable chunks. This makes it simpler to handle different aspects of our platform, like categories, products, and user profiles.

![Database Schema](docs/readme_images/database-schema.png)

### Security Features
#### User Authentication
To ensure safe and easy user access, Django Allauth is implemented for user authentication, allowing users to securely log in and manage their accounts.

#### Form Validation
If the submitted form is not valid, an error will accour telling the user what field is missing or is incorrect.
If any submitted form is not valid or contains errors, users will receive a clear error message, showing which fields is causing the error.

#### Custom 404 error page
![404 Page](/docs/readme_images/404page.png)
If a user come across a wrong URL, they will be directed to a custom 404 error page, allowing the user to easily go back to the homepage.

#### Database Security
Sensitive information, such as database URLs, secret keys, stripe keys, webhook secrets, AWS credentials, and email access, are stored securely in the env.py file to prevent unauthorized access.

## Features

### Header
![Header](/docs/readme_images/header.png)

#### Logo
- A logo was created in Canva, using the fonts Libre Baskerville and Brittany.
- The logo is positioned in the top left of the site, and is linked to the home page for an easier navigation for the site user.


#### Navigation Bar

- The header and navigation bar are present on every page and include every link to the other pages.
- The navigation menu includes three different dropdown menus allowing the user to browse products sorted by '"Room, "Color", "Pattern" and "Latest Deals".
- The navigation menu also includes a link to the Services page, where the user can book an appointment with one of our experts, and a link to the FAQ page.
- The navigation bar is fully responsive, transforming to a hamburger symbol on smaller screens and devices.

#### Search Bar

- The search bar is displayed above the navigation links.
- On smaller screens and devices, the search bar becomes a search icon. Clicking it will show the full search bar.
- When entering a word in the search bar, all products containing that word in their title or description, will be presented in the search results.

#### User Icon 

- When users are not signed in, the user icon displays a dropdown menu offering the options "Register" and "Log in".
- Once users are signed in, the user icon shows a dropdown menu with the choices "My Profile" and "Log Out".
- Additionally, for signed-in site administrators, the user icon provides the option "Product Management", giving access to add products or services.

#### Bag Icon

- Positioned to the right of the user icon, users will find the bag icon.
- The bag manages the items in the user's bag, with the total cost visible underneath.
- Whenever users add, delete, or edit items in their bag, a toast message notifies them of the success or failure of their action.
- Clicking on the bag icon allows users to view the contents of their bag, along with prices and the remaining amount required for free delivery.
- When clicking the bag icon, users have the option to proceed to a page where they can view their bag and proceed to the checkout process.

### Footer

![Footer](/docs/readme_images/footer.png)

- The footer is present at the bottom of every page across the site.
- The footer features links to the site's social media profiles on Facebook, LinkedIn, Instagram, and Pinterest.
- Additionally, the footer includes a signup section for the MailChimp Newsletter, enabling users to subscribe and receive updates on the latest deals and offers.
- Other footer links include access to the products page, services page, FAQ page, Custom Reviews, and the Privacy Policy.
- All external links automatically opens in a new tab.

### Home Page
![The Home Page](/docs/readme_images/home-page.png)
- The homepage features a big image, showing the visitors a wallpaper from the newest collection.
- A section on the homepage informs users about the website's purpose.
- Towards the bottom of the homepage, two images provide easy access to products categorized under "By Room" and "By Pattern".

### Profile Page

##### Delivery Information
![Delivery Information](/docs/readme_images/delivery-information.png)

- The delivery details section saves the user's delivery address and phone number.
- This information is used to fill in the users delivery address automatically when they are accessing the check out.

##### Order History

![Order history](/docs/readme_images/order-history.png)
- The order history section shows a list of all orders placed by the user.
- Each order includes the order number, date of purchase, item details, and total cost.
- When clicking on the order number, it redirects the user to a page summarizing the order details.

##### Booked Services

![Booking History](/docs/readme_images/booking-history.png)
- Below the Order History, users can find a section listing all booked appointments.
- Each booking displays a booking ID, appointment date, booked service, and forthcoming cost.
- When clicking on the booking ID, it redirects the user to a page summarizing the booking details.

#### Wishlist
![Wishlist](/docs/readme_images/wishlist.png)
- Located below the Booked Services, users can find a section listing all products they've added to their wishlist.
- Each wishlist item displays the product title and image.
- When clicking on the product in the wishlist, it redirects the user to the product detail page.

### User Account Pages

- Django allauth was installed and used to implement the Sign up, Log in, and Log out functionality. 
- Success messages notify users of successful login/logout actions.
- When the user is register for an account, the user must verify their email address by clicking on the authentication link sent to the provided email address.
- Users can reset their password by clicking on the 'Forgot Password' link on the login page if they forget it.

### The Categories Pages
![Categories Pages](/docs/readme_images/categories.png)
- Under the "Latest Deal" menu, users can choose from different categories such as "New In," "Bestsellers," "Last Chance," and "View all," each redirecting them to the product page.
- In the other dropdown menus within the navigation bar, users can select categories. If they want to see all products in a specific category, they will be lead to a page where they can further filter by subcategories.
- The visibility of products depends on the category selected by the user.
- Every product is displayed with an image, title, rating and price.

### The Products page
![Products](/docs/readme_images/products.png)
- When clicking on a product, the user will get transfered to a page featuring a more detailed information about the product.
- Alongside the title, rating, and price, users will find a detailed product description.
- Each product description provides helpful information about measurements, helping users choose the right amount.
- If the user is unsure about sizing and quantity, a link is provided for users to schedule a meeting with an expert for personalized advice.
- The user can adjust the quantity and add the product to their shopping bag.
- If the user is logged in they can also add products to their wishlist, that is accessible in their profile that can be found under the user icon.
- If the user is a site administrator an edit and delete button will also appear in the product details.

### Services Page
![Service](/docs/readme_images/service.png)
- Every service is displayed with an image, title, description and price.
- Clicking on a service redirects the user to a page providing detailed information about the service.
- Below the service description, users find a booking form to schedule appointments.
- After booking an appointment, users receive a success message confirming that the booking was successful.
- After booking the appointment, the user are directed to a page summarizing the appointment details.
- Payment for appointments is not required in advance, allowing users to schedule meetings without upfront payment.


### Product and Service Management

#### Add Product

- Only site administrators and superusers can create and add products.
- Access the "Product Management" option from the dropdown menu under the user icon to reach the add product page.
- The service form must be valid to add a service, and every required field is marked with an asterisk (*).
- Product prices must be greater than 0 and cannot exceed 6 digits in total.
- The user have the option to upload an image for the product. If no image is provided, a default image is displayed.
- Once the form is filled out and validated, the product can be created by clicking the add button.
- The user will receive a success message confirming that the product has been successfully added.

#### Edit Product

- Only site administrators and superusers can edit products.
- The user can access the edit page by clicking the "Edit" button located either under the product or within the product details.
- When opening the edit form, all fields are pre-populated with their original content.
- The image field presents a preview of the existing image, along with a checkbox option to remove it. Selecting this checkbox will replace the image with the default one.
- The user will receive a success message confirming that the product has been successfully edited.

#### Delete Product

- Only site administrators and superusers can delete products.
- The user can delete the product by clicking the "Delete" button located either under the product or within the produt details.
- Upon clicking "Delete," a confirmation modal will appear, asking the user to confirm the deletion.
- The user will receive a success message confirming that the product has been successfully deleted.

#### Add Service

- Only site administrators and superusers can create and add services.
- Access the "Product Management" option from the dropdown menu under the user icon to reach the add service page.
- The service form must be valid to add a service, and every required field is marked with an asterisk (*).
- Service prices must be greater than 0 and cannot exceed 6 digits in total.
- The user have the option to upload an image for the service. If no image is provided, a default image is displayed.
- Once the form is filled out and validated, the service can be created by clicking the add button.
- The user will receive a success message confirming that the service has been successfully added.

#### Edit Service

- Only site administrators and superusers can edit services.
- The user can access the edit page by clicking the "Edit" button located either under the service or within the service details.
- When opening the edit form, all fields are pre-populated with their original content.
- The image field presents a preview of the existing image, along with a checkbox option to remove it. Selecting this checkbox will replace the image with the default one.
- The user will receive a success message confirming that the service has been successfully edited.

#### Delete Service

- Only site administrators and superusers can delete services.
- The user can delete the service by clicking the "Delete" button located either under the service or within the service details.
- Upon clicking "Delete," a confirmation modal will appear, asking the user to confirm the deletion.
- The user will receive a success message confirming that the service has been successfully deleted.

### Bag
![Bag](/docs/readme_images/bag.png)
- Clicking on the bag icon in the navigation menu redirects the user to the shopping bag page, where they can view the contents of their cart.
- The bag displays product information including the image, description, price, and quantity.
- The user can adjust the quantity by clicking the plus or minus buttons.
- Products with a quantity less than 0 are automatically removed from the bag.
- To update the quantity, users can click the "Update" button.
- To remove a product, users can use the "Remove" button.
- Below the product information, users can view the total cost of the bag, delivery cost, and grand total.
- If there is any remaining spending required for free delivery, that is also provided. 
- The user can then choose to continue shopping or proceed to secure checkout by clicking the respective buttons.

### Checkout 

#### Details Section
![The Checkout Form](/docs/readme_images/checkout-form.png)
- In the details section, users can input their contact information, delivery address, and card details.
- If the user is not logged in or doesn't have an account, a link to login or create an account will be provided.
- The user also have the option to make a purchase as a guest.
- For signed-in users who haven't saved their information, there's a checkbox to save the delivery information.
- Logged-in users who have opted to save their information will find their details pre-filled.
- If any required fields are left blank, an error message will appear, asking the user to fill them in.
- All required fields are marked with an asterisk (*).

#### Order Summary 
![Order Summary](/docs/readme_images/order-summary.png)
- The order summary section provides an overview of the products to be purchased, including their details.
- It showcases the product name and image, quantity, subtotal, delivery cost, and grand total.products and the subtotal, delivery and grandtotal. 
- Clicking on the product image within the order summary redirects the user to the respective product detail page.

#### Payment 

- The payment system is powered by Stripe to ensure secure transactions.
- Invalid card numbers will trigger an error message for the user to correct the issue.
- During payment processing, a loading screen is displayed, preventing the user from navigating away.
- A warning message is displayed at the bottom of the page, informing the user of the expected charge amount.
- Even if the payment form fails to submit or the user closes the browser during processing, orders are still created in the database through a webhook
- After the payment is processed, the webhook verifies order existence in the database. If not found, it creates one using payment details.

#### Confirmation
![Order Confirmation](/docs/readme_images/order-confirmation.png)
- After the order is processed, the user is directed to the checkout success page.
- On the checkout success page, the completed order is summarized.
- Additionally, an email containing the order confirmation will be sent to the user.
- Finally, at the end of the summary, a "Keep Shopping" button allows the user to return to the product page.

### Frequently Asked Questions (FAQ)
![FAQ Page](/docs/readme_images/faq.png)
- The FAQ page provides answers to common questions that our customers frequently ask.
- The user can easily navigate through various questions to find the information they need.
- At the bottom of the FAQ page, the user can find contact information in case they have additional questions or inquiries.

### Customer Reviews
![Customer Reviews](/docs/readme_images/customer-reviews.png)
- The user can access our customer reviews page located in the footer of our website.
- On this page the user can explore feedback and testimonials from previous customers to gain insights into their experiences.
- The user can share their own thoughts and feedback by filling out a simple form with their name and comments.

## Business Model 

HappyRoom operates under a B2C (Business to Consumer) model, selling products and services directly to end-users, who are our customers.

Our typical customers are homeowners, mainly adults or families seeking to redecorate their living spaces.

## Marketing Strategy

HappyRoom uses different marketing strategies to connect with its audience, including SEO, content marketing, social media marketing, and email marketing.

### SEO

We carefully choose keywords, both short and long, after studying Google search results and our competitors' strategies. These keywords are added to our website's meta keywords and descriptions to improve our search engine ranking.

| Keyword | Related Keywords |
|---------|------------------|
| Wallpaper | Modern Wallpaper, Aesthetic Wallpaper, Cute Wallpaper, Peel & Stick Wallpaper, Luxury Wallpaper, Custom Wallpaper, Design Wallpaper |
| Room | Kitchen, Livingroom, Bedroom, Kidsroom, Room designer, Romantic Bedroom Wallpaper, Room decor ideas |
| Interior | Interior room, Interor design, Interior Diy, Inspiration interior, Wallpaper design 3d, Wallpaper shops, Wallpaper Store |

#### Building Trust

We include a customer reviews page where users can read reviews and comments from previous customers. Additionally, links to both the customer reviews and privacy policy are included in the footer to inform users about how their data is being collected and processed.

#### Sitemap and robots.txt

To make search engine navigation easier, a sitemap was created, listing important page URLs using xml-sitemaps.com. Additionally, a robots.txt file is created to specify areas of the website that search engines should avoid, enhancing overall site quality for SEO purposes.

### Content Marketing

We showcase high-quality images of our interior design projects to attract potential clients and build trust. These photos highlight our expertise and unique styled wallpapers.

#### Social Media Marketing

Social media marketing is used through platforms like Facebook, Instagram, and Pinterest because many people seek inspiration there. This complements  the content marketing, as we can easily share images of past projects and new products. We also run sales and offer discounts through ads on these platforms to catch our customers attention.

![HappyRoom Facebook Page ](docs/readme_images/happyroom-facebook.png)

#### Email Marketing

Additionally, our users can sign up for our newsletter to receive news, updates, and deals. We use Mailchimp to manage this service, making it easy for us to stay connected with our customers.

Overall, by using a mix of these strategies, HappyRoom aims to reach more people, bring more traffic to the website, and increase both sales and brand awareness.

Understanding our users' needs is our top priority. 
They want clear information, guidance, and inspiration, so we provide useful content like inspiring pictures and helpful guides. Our business goals shape our marketing strategies, to meet these goals effectively.

# TESTING 

#### User Story Testing 

 - All user stories have been tested out and are working correctly. 
 - All user stories related to site owner and site administration have been tested out and are working correctly.


## Validator Testing 

### W3C Validator HTML
All HTML pages were tested through the [W3C HTML Validator](https://validator.w3.org/). 

No errors were found on these pages:
- Index Page.
- Product Page.
- Category Page.
- Subcategory Page.
- Checkout Page.
- Checkout Success Page.
- Bag Page.
- Services Page.
- Service Details Page.
- Order Confirmation Page.
- Booking Confirmation Page. 
- Profile Page.
- Customer Reviews Page. 
- FAQ Page. 
- 404 Error Page. 

When validating these pages a few errors occured: 
- Register Page.
  - An error indicating that the element ul is not allowed as a child of the element small. This error is related to the Django Allauth templates and was left unfixed.

- Add Product & Service Page. 
  - When validating this page, 28 errors and warnings were encountered, all related to the forms. These errors were left unfixed as they are not critical for the website's functionality. Screenshots of these errors and warnings are provided below.

![W3C Validator HTML Errors ](docs/readme_images/w3c-error-1.png)
![W3C Validator HTML Errors ](docs/readme_images/w3c-error-2.png)
![W3C Validator HTML Errors ](docs/readme_images/w3c-error-3.png)
![W3C Validator HTML Errors ](docs/readme_images/w3c-error-4.png)
![W3C Validator HTML Errors ](docs/readme_images/w3c-error-5.png)

### W3C Validator CSS
The CSS files were tested using the [W3C Validator CSS](https://jigsaw.w3.org/css-validator/) with no errors found.

### JS Hint 

All JavaScript were tested using the [Jshint validator](https://jshint.com/) with no errors.


### PEP8

All Python were tested through the [CI Python Linter](https://pep8ci.herokuapp.com/) except for in the settings file where a few lines were too long. These were left as is since the importance of the settings being correct outweighed the issue of line length.

![CI Python Validator - Settings](docs/readme_images/ci-python-linter.png)


## Lighthouse 

## Lighthouse 

When I checked my website's performance with the Lighthouse tool, I noticed it wasn't doing as well as I hoped, especially in performance and best practices.
Despite having already optimized the images, it seems other things are slowing down how quickly the website loads.
I suspect that elements such as Javascript and CSS may be contributing to the slowdown. 
Addressing these issues would likely improve the website's performance and provide a better user experience.

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| DESKTOP        |              |               |                 |     |
| Home Page      |           94 |            90 |              86 | 100 |
| Profile Page    |           97 |            89 |              95 | 100 |
| Product Page   |           97 |            90 |              91 | 100 |
| Product Detail Page     |           99 |            97 |              95 | 100 |
| Services Page    |           94 |            86 |              86 | 100 |
| Service Detail Page    |           98 |            94 |              95 | 100 |
| Bag      |           97 |            89 |              95 | 100 |
| Checkout Page      |           97 |            89 |              95 | 100 |
| Log in Page|           99 |            88 |              95 | 100 |
| Log out Page       |           98 |           100 |              95 | 100 |
| Register Page   |           95 |           89 |             95 | 100 |
| Customer Review Page   |           97 |            95 |              91 | 100 |
| FAQ Page  |          100  |           94 |              95 |  100 |
| Edit Product      |           97 |            89 |              95 | 100 |
| Edit Service      |           97 |            89 |              95 | 100 |
| Add Product/Service      |           97 |            89 |              95 | 100 |
| 404 Error Page      |           97 |            89 |              95 | 100 |
|                |              |               |                 |     |
| MOBILE         |              |               |                 |     |
 Home Page      |           94 |            90 |              86 | 100 |
| Profile Page    |           97 |            89 |              95 | 100 |
| Product Page   |           97 |            90 |              91 | 100 |
| Product Detail Page     |           99 |            97 |              95 | 100 |
| Services Page    |           94 |            86 |              86 | 100 |
| Service Detail Page    |           98 |            94 |              95 | 100 |
| Bag      |           97 |            89 |              95 | 100 |
| Checkout Page      |           97 |            89 |              95 | 100 |
| Log in Page|           99 |            88 |              95 | 100 |
| Log out Page       |           98 |           100 |              95 | 100 |
| Register Page   |           95 |           89 |             95 | 100 |
| Customer Review Page   |           97 |            95 |              91 | 100 |
| FAQ Page  |          100  |           94 |              95 |  100 |
| Edit Product      |           97 |            89 |              95 | 100 |
| Edit Service      |           97 |            89 |              95 | 100 |
| Add Product/Service      |           97 |            89 |              95 | 100 |
| 404 Error Page      |           97 |            89 |              95 | 100 |

## Browser Testing

The website has been tested across various browsers, including Google Chrome, Safari, and Firefox. All functionalities are working correctly across these browsers.

## Device Testing

The website has been tested on a range of devices, including iPhone, iPad, MacBook Pro, and iMac. The website is fully functional and displays properly across all tested devices.

## Responsiveness

The website's responsiveness has been tested through the Google Chrom Dev Tool and [Am I Responsive?](https://ui.dev/amiresponsive), and is working correctly.

## Manually Testing 

#### Home Page
- Each link on the home page has been thoroughly tested and is working correctly.

 #### Account Links
 - All account pages have been tested and are working correctly.
- Both the login and signup forms have been tested and are functioning without any issues.

#### Profile Page
- The profile page has been tested and is working correctly.
- Thhe details form has been thoroughly tested and is saving information correctly.
- The Order History section is working correctly, with links seamlessly transferring users to the order detail page. 
- The Booking History section is working correctly, with links seamlessly transferring the user to the booking detail page. 
- The Wishlist section is working correctly, with images serving as links to product details.

#### Product Management Page
- The add product or add service form has been tested and is operating correctly.
- In case of invalid inputs, the system generates error messages, making sure everything works smoothly for the user.

#### Customer Reviews Page
- The Leave a Review form has been tested and is working correctly. 

#### Footer 
- All links in the footer have been tested and are working correctly.
- The Social Media Icons are functioning correctly, redirecting users to the different pages.
- All Social Media links will open in a new tab for a better user experience.
- The Newsletter sign-up functionality has been tested and is working correctly. 

#### Products
- Both product pages and category pages have been tested and are operating without any issues.
- All links on these pages have been tested and are working correctly.


#### Product Detail Page
- The product detail page have been tested and is working correctly. 
- The Quantity button on the product has been thoroughly tested and is functioning.
- The Add to Bag and Add to Wishlist buttons have been tested and are working correctly.

#### Service Page
- The Service page have been tested and is working correctly.
- The links to services are working correctly, seamlessly redirecting users to the service detail page.

#### Service Detail Page
- The Service detail page have been tested and is working correctly. 
- The Booking form has been tested and is working , only accepting valid inputs.
- When booking a service, users are seamlessly redirected to a booking detail page.

#### Bag Page

- The Bag page have been tested and is working correctly. 
- All links and buttons on the page have been tested and are functioning correctly.

#### Checkout Page

- The checkout page has been tested and is working correctly. 
- The checkout form has been tested and is only functional with valid inputs. In case of errors, clear instructions are provided to the user.
- The payment method functionality has been tested and is working correctly.

#### Messages 
  - Toast messages providing feedback on user actions have been tested and are working correctly.
  - The delete confirmation modal has been tested and is functioning.

## Bugs and Issues

### Unfixed Bugs and Issues
During the validation process of the Registration page and Add Product & Service page, several issues were identified:

- An error was occurring, indicating that the "ul" element is not allowed as a child of the "small" element. This issue is present in the Django Allauth templates and therefore has been left unfixed.

- Validation of the Add Product & Service page revealed 28 errors and warnings. 
These errors mainly come from how the form is set up. For instance, the {% csrf_token %} tag and the way the form fields are looped through,may be the reasons behind these errors. 
However, even with these errors, the main functions of the page, like submitting the forms, still works correctly. As a result, these errors have been left unfixed for now.
However, I will carefully consider addressing them in future improvements.

## Deployment - Heroku
The website was deployed through the hosting platform Heroku, from its GitHub repository.

### Create the Heroku App
- Create an account or log in to [Heroku](https://dashboard.heroku.com/apps).
- On the main page click "New" at the top right corner and choose "Create New App" from the dropdown menu.
- Give the app a unique and meaningful name.
- Next up, select your region.
- Click "Create App".

### Connect the Postgres database
- In the Resources tab, type "Postgres", and select "Heroku Postgres".
- Copy the DATABASE_URL from Config Vars in the Settings Tab.
- Install two additional requirements in your IDE:
   - pip3 install dj_database_url
   - pip3 install psycopg2-binary
- Create a requirements.txt file.
- Create an env.py file in the main directory of your GitPod workspace.
- Add the DATABASE_URL value and your personally selected SECRET_KEY value to the env.py file.
- Update your settings.py file to import the env.py file and add the paths for both the DATABASE_URL and SECRET_KEY.
- Comment out the default database configuration.
- Save your files and run the migrations. 
- Create a superuser.
- Create an if statement in settings.py to run the Postgres database when using the app on Heroku or SQLite.
- Create the requirements.txt file
- Create a file named "Procfile" in the main directory of your project.
- In "Procfile" add "web: gunicorn project-name.wsgi".
- Add Heroku to your ALLOWED_HOSTS.

#### Update the Heroku Config Vars
- In Heroku, add these Config Vars:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - DATABASE_URL
  - EMAIL_HOST_PASS
  - EMAIL_HOST_USER
  - SECRET_KEY
  - STRIPE_PUBLIC_KEY
  - STRIPE_SECRET_KEY
  - STRIPE_WH_SECRET
  - USE_AWS

### Deploy your site
- Before deploying, make sure that your DEBUG is set to false in your settings.py file.
- Go to the deploy tab on Heroku, navigate to connect to GitHub, and then pick the required repository.
- Scroll to the bottom of the page where you can choose if you want to Enable Automatic Deploys for 

- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll down to the bottom of the page and there you can choose if you want the deploys to be Automatic or Manually. The Manually deployed branches need redeploying each time the repository is updated.
- Deploy your website. 
- Click "View", or scroll up to "Open App" to visit the deployed site.

The deployed website can be found here - [HappyRoom](https://happy-room-e68715746875.herokuapp.com/).

## AWS
### AWS S3 Bucket
- Create an AWS Account:
  - Visit the AWS Management Console and sign up for an account.
- In the AWS Management Console, navigate to the 'S3' service.
- Click 'Create a new bucket' and choose the region closest to you.
- Enable 'ACLs' under 'Object Ownership' and keep the Object Ownership as 'Bucket owner preferred'
- Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Navigate to the 'Properties' tab within the created bucket. Scroll down to the bottom and find the 'Static website hosting' section. Click on 'edit' and set the Static website hosting option to 'enabled'. 
- Copy the default values for the index and error documents and click 'save changes'.
- Move to the 'Permissions' tab. Locate the CORS configuration section and insert the following code:

      [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
      ]
- In the 'Bucket Policy' section, choose 'Policy Generator'.
- From the dropdown select 'S3 Bucket Policy' and add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Navigate to the 'Access Control List' section, click edit, enable List for Everyone (public access), and confirm the warning.

### IAM
- From the 'Services' menu, search for the service IAM.
- On the IAM page, on the sidebar click on 'User Groups' and then 'Create group'.
- Go to 'Policies', click on 'Create New Policy', and go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search for 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Find the bucket ARN from the 'S3 Permissions' section.
- Remove the '*' from the 'Resource' key and replace it with your bucket ARN in two places.
- After that, go through the steps to review and create your policy.
- In the 'User Groups' section, open the group you created and add permissions by attaching the policies you've created.
- Create a user for the group by selecting users from the sidebar and clicking 'Add user'.
- Provide a username and check the box for 'Programmatic Access'.
- Follow the prompts until you reach the 'Create user' button, then click it.
- Finally, download the CSV file containing your AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID, which you'll need for Heroku variables and your env.py file.

### Connecting S3 to Django 
- Go back to your IDE and install two more requirements: 
  - boto3
  - django-storages.
- Update the requirements.txt file with the new dependencies.
- Then add 'storages' to your installed apps.
- In the settings.py file, create an if statement to check if 'USE_AWS' is in the environment variables.
- Inside the if statement, set up your AWS credentials including the bucket name, region, access key, and secret key, to let django know where to look for the static files in production.
- Create a file named custom_storages and define two classes: 
   - StaticStorage
   - MediaStorage
- In settings.py, specify the storage classes for static files and media files, and settings for AWS S3 objects.
- Navigate to your S3 bucket, create a folder named 'media', and upload all your media files into this folder.
- Make sure to grant public-read access to these files under the 'Permissions' section.
- Django should now automatically link your static and media files to your S3 bucket.


## Languages

- Python
- HTML5
- CSS3
- Javascript


## Frameworks, Libraries and Programs Used
- [Django](https://www.djangoproject.com/): The main framework used in this project, built with Python.
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): The authentication library used for creating user accounts in this project.
- [PostgreSQL](https://www.postgresql.org/): Used as the database for this project.
- [JQuery](https://jquery.com/)
- [Stripe](https://stripe.com/ie): Used for the payments system.
- [AWS](https://aws.amazon.com/?nc2=h_lg): Used for file storage.
- [GitHub](https://github.com/): Used as agile tool.
- [Heroku](https://dashboard.heroku.com/login): Hosting the live website.
- [Bootstrap](https://getbootstrap.com/): Used as the main front-end framework.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used to manage all Django Forms.
- [Sitemap Generator](www.xml-sitemaps.com): Used to create sitemap.xml. 
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used to create the site's privacy policy.
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.
- [FlatPickr](https://flatpickr.js.org/themes/): Used for the date picker in booking form.

### Additional Programs Used

- [Font Awesome](https://fontawesome.com/): Used for icons in the footer, and on comments.
- [Google Fonts](https://fonts.google.com/): Used to import fonts, elevating the layout of the project.
- [Am I Responsive?](https://ui.dev/amiresponsive)
- [Balsamiq](https://balsamiq.com/): Used to generate the Wireframe images.
- [W3C](https://www.w3.org/): Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/): Used to validate all javascript.
- [Color Space](https://mycolor.space/): Used to create the color palette.
- [Favicon](https://favicon.io/): Used to create the favicon.
- [Grammerly](https://app.grammarly.com/): Used to proof read the README.md. 
- [Canva](https://www.canva.com/sv_se/): Used to create the logo. 

## Credits
 - [Stack Overflow](https://stackoverflow.com/)
 - [W3Schools](https://www.w3schools.com/django/)
 - [Django Project](https://docs.djangoproject.com/)
 - [Bootstrap Documentation](https://getbootstrap.com/)
 - [DEV](https://dev.to/)
 - [REINTECH](https://reintech.io/)
 - [Quora](https://djangowebdevelopers.quora.com/)
- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
- Every product detail, service detail and FAQ is created with [Open AI](https://chat.openai.com/).
- Tutor Support, Code Institute, for their support and advice.
- My mentor Antonio, for all of his knowledge, support, and advice.