// Import jQuery
import $ from 'jquery';
import Masonry from 'masonry-layout';
import AOS from 'aos'; // Import AOS library

$(document).ready(function() {
    AOS.init();

    // Navbar scroll effect
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $('#main-nav').addClass('bg-white shadow-md');
        } else {
            $('#main-nav').removeClass('bg-white shadow-md');
        }
    });

    // Mobile menu toggle
    $('#mobile-menu-button').click(function() {
        $('#mobile-menu').toggleClass('hidden');
    });

    // Testimonial carousel
    $('.testimonial-carousel').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 640,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    // Theme switcher
    $('.theme-image').hover(function() {
        var theme = $(this).data('theme');
        $('body').removeClass('theme-wedding theme-marriage theme-birthday').addClass('theme-' + theme);
    });

    // Image pop-up
    $('.gallery-image').click(function() {
        var src = $(this).attr('src');
        var description = $(this).data('description');
        
        $('body').append(`
            <div class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50" id="image-popup">
                <div class="bg-white p-4 rounded-lg max-w-3xl">
                    <img src="${src}" alt="Gallery Image" class="w-full h-auto">
                    <p class="mt-4 text-lg">${description}</p>
                    <button class="mt-4 bg-primary text-white px-4 py-2 rounded" id="close-popup">Close</button>
                </div>
            </div>
        `);
    });

    $(document).on('click', '#close-popup', function() {
        $('#image-popup').remove();
    });

    // Initialize Masonry for the gallery grid
    if ($('#gallery-grid').length) {
        var msnry = new Masonry('#gallery-grid', {
            itemSelector: '.gallery-item',
            columnWidth: '.gallery-item',
            percentPosition: true
        });

        // Layout Masonry after all images have loaded
        imagesLoaded('#gallery-grid').on('progress', function() {
            msnry.layout();
        });
    }
});

// Add any custom JavaScript here
document.addEventListener('DOMContentLoaded', function() {
    // Example: Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});