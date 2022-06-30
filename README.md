<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kostyafarber/car-sales">
    <img src="images/puzzle.png" alt="Logo" width="40" height="40">
  </a>

<h3 align="center">Car Prices Scraper</h3>

  <p align="center">
    This project scrapes car prices every morning using AWS Lambda and stores them in a DynamoDB table. I used this to help me sell my car before I moved to London from Sydney.
    <br />
    <a href="https://github.com/kostyafarber/car-sales"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kostyafarber/car-sales">View Demo</a>
    ·
    <a href="https://github.com/kostyafarber/car-sales/issues">Report Bug</a>
    ·
    <a href="https://github.com/kostyafarber/car-sales/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://nextjs.org/)
* [AWS](https://reactjs.org/)
* [BeautifulSoup](https://vuejs.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Motivation

This is a project I started when I was trying to sell my car before my move to London. I needed to get a feel for what the car market prices were for my Mazda. 

I scraped car sales prices using BeautifulSoup and used AWS Lambda to trigger my code every morning. The results were stored in AWS DynamoDB which then sent an email to my inbox notifying me of the median, mean and price. This helped me make a data-driven sale by setting a fair price.

### Prerequisites

The lambda function is in `src/scraper/lambda_function.py` and follows the standard AWS Lambda structure.

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Email: kostya.farber@gmail.com

Project Link: [https://github.com/kostyafarber/car-sales](https://github.com/kostyafarber/car-sales)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kostyafarber/car-sales.svg?style=for-the-badge
[contributors-url]: https://github.com/kostyafarber/car-sales/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kostyafarber/car-sales.svg?style=for-the-badge
[forks-url]: https://github.com/kostyafarber/car-sales/network/members
[stars-shield]: https://img.shields.io/github/stars/kostyafarber/car-sales.svg?style=for-the-badge
[stars-url]: https://github.com/kostyafarber/car-sales/stargazers
[issues-shield]: https://img.shields.io/github/issues/kostyafarber/car-sales.svg?style=for-the-badge
[issues-url]: https://github.com/kostyafarber/car-sales/issues
[license-shield]: https://img.shields.io/github/license/kostyafarber/car-sales.svg?style=for-the-badge
[license-url]: https://github.com/kostyafarber/car-sales/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kostyafarber
[product-screenshot]: images/carsales-logo.png
