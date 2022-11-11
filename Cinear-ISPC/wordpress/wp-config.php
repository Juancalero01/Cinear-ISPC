<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress1' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'um x%g&F]p[:Uxi}#Skvd[6VxgCF7&Pb55<.xAKQ7hbq#Z?IL]6&ZlVL 15i0UI%' );
define( 'SECURE_AUTH_KEY',  '%Cnr`&+^G2v%~:G|(XHtRfCzQ0!tN&P9|d|2PqN7hb4c^:S+x+jYCd`-+ORH?/J,' );
define( 'LOGGED_IN_KEY',    'mNJs]?sk{/3S qH~UK:-{n~TKS~-rt!tx4Nb?^_`v(U&1a,`;k.!O7s,v|s>Cd/|' );
define( 'NONCE_KEY',        'o?Wg80) EarqxW<Bo?a,|F**:M2RzHtIAy:35Ty;d1R{#pK*7ev3LW4IucwH|9!k' );
define( 'AUTH_SALT',        '#UOc_jI*O`S^Nm)|~~i/i-5!:=8Q9N{8_.v|L y2jT_/)3~O8r@>`Xeo?,.0:Hf:' );
define( 'SECURE_AUTH_SALT', 'WM317v)E{Ge?L*_n_jE)}{~xSfnEm@u[;4.{`hguo-y)p532){PH(C%k,i|X{Lk%' );
define( 'LOGGED_IN_SALT',   '9Zulg2|tD9;%j7aveAN6p +-TPl_kB0 HY1gjY9+YGmZ%&t!O0!djV>a3QRYaaKl' );
define( 'NONCE_SALT',       'r,a/$n#JOLW?j]B7?{b+nL0 ;7,[1/z-v>Aj7C#6]`8# og@{HkxQp]s|+Ulq2td' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
