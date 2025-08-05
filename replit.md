# Radha Madhav Transport Company Website

## Overview

This is a Flask-based business website for Radha Madhav Transport Company, a logistics and transportation service provider operating across Uttar Pradesh, India. The website serves as a digital presence to showcase the company's 15+ years of experience, fleet of 20+ containers, comprehensive transport services, and network coverage throughout the state.

The application is a traditional server-side rendered website using Flask templating, designed to provide information about services, company history, and facilitate customer contact through an inquiry form.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Animation Library**: AOS (Animate On Scroll) for page animations
- **Icons**: Font Awesome 6.4.0 for consistent iconography
- **Fonts**: Google Fonts (Poppins) for typography
- **JavaScript**: Vanilla JavaScript for interactive components

### Backend Architecture
- **Web Framework**: Flask (Python) with minimal configuration
- **Routing**: Simple route-based navigation for static pages
- **Session Management**: Flask sessions with secret key configuration
- **Form Handling**: Basic contact form processing with validation
- **Logging**: Python logging module for debugging

### Page Structure
- **Multi-page Application**: Seven main pages (Home, About, Services, History, Why Choose Us, Network, Contact)
- **Template Inheritance**: Base template with shared header/footer/navigation
- **Responsive Design**: Mobile-first approach using Bootstrap grid system
- **SEO Optimization**: Proper meta tags, breadcrumbs, and semantic HTML

### Design Patterns
- **MVC Pattern**: Clear separation between routes (controllers), templates (views), and minimal data handling
- **Template Inheritance**: DRY principle applied through base template
- **Component-based CSS**: Modular CSS with custom properties and component classes
- **Progressive Enhancement**: JavaScript adds interactivity without breaking core functionality

### Contact Form Processing
- **Basic Validation**: Server-side validation for required fields
- **Flash Messaging**: User feedback through Flask flash messages
- **No Database**: Currently handles form submissions without persistence
- **Form Fields**: Name, email, phone, service type, and message

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.3.0**: UI framework via CDN
- **Font Awesome 6.4.0**: Icon library via CDN
- **AOS 2.3.4**: Animation library via CDN
- **Google Fonts**: Poppins font family

### Python Dependencies
- **Flask**: Core web framework
- **Jinja2**: Template engine (included with Flask)

### Static Assets
- **External Images**: Pixabay URLs for placeholder content
- **Custom CSS**: Local stylesheet for brand-specific styling
- **Custom JavaScript**: Local scripts for enhanced interactivity

### Environment Configuration
- **SESSION_SECRET**: Environment variable for Flask session security
- **Development Server**: Flask development server configuration

### Missing Production Dependencies
- **Web Server**: No production WSGI server configured
- **Database**: No database integration for contact form persistence
- **Email Service**: No email sending capability for contact form submissions
- **SSL/HTTPS**: No security configuration
- **Static File Serving**: Relies on Flask for static file serving