FROM php:8.2-apache

WORKDIR /var/www/html/
# doplnění podpory mysql do php
RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN chown -R www-data:www-data /var/www/html/
RUN chmod -R 755 /var/www/html/