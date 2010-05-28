begin_unit
comment|'# -*- test-case-name: twisted.test.test_nmea -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""NMEA 0183 implementation\n\nMaintainer: Bob Ippolito\n\nThe following NMEA 0183 sentences are currently understood::\n    GPGGA (fix)\n    GPGLL (position)\n    GPRMC (position and time)\n    GPGSA (active satellites)\n \nThe following NMEA 0183 sentences require implementation::\n    None really, the others aren\'t generally useful or implemented in most devices anyhow\n\nOther desired features::\n    - A NMEA 0183 producer to emulate GPS devices (?)\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'operator'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'basic'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'compat'
name|'import'
name|'reduce'
newline|'\n'
nl|'\n'
name|'POSFIX_INVALID'
op|','
name|'POSFIX_SPS'
op|','
name|'POSFIX_DGPS'
op|','
name|'POSFIX_PPS'
op|'='
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
newline|'\n'
name|'MODE_AUTO'
op|','
name|'MODE_FORCED'
op|'='
string|"'A'"
op|','
string|"'M'"
newline|'\n'
name|'MODE_NOFIX'
op|','
name|'MODE_2D'
op|','
name|'MODE_3D'
op|'='
number|'1'
op|','
number|'2'
op|','
number|'3'
newline|'\n'
nl|'\n'
DECL|class|InvalidSentence
name|'class'
name|'InvalidSentence'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|InvalidChecksum
dedent|''
name|'class'
name|'InvalidChecksum'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|NMEAReceiver
dedent|''
name|'class'
name|'NMEAReceiver'
op|'('
name|'basic'
op|'.'
name|'LineReceiver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This parses most common NMEA-0183 messages, presumably from a serial GPS device at 4800 bps\n    """'
newline|'\n'
DECL|variable|delimiter
name|'delimiter'
op|'='
string|"'\\r\\n'"
newline|'\n'
DECL|variable|dispatch
name|'dispatch'
op|'='
op|'{'
nl|'\n'
string|"'GPGGA'"
op|':'
string|"'fix'"
op|','
nl|'\n'
string|"'GPGLL'"
op|':'
string|"'position'"
op|','
nl|'\n'
string|"'GPGSA'"
op|':'
string|"'activesatellites'"
op|','
nl|'\n'
string|"'GPRMC'"
op|':'
string|"'positiontime'"
op|','
nl|'\n'
string|"'GPGSV'"
op|':'
string|"'viewsatellites'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPVTG'"
op|':'
string|"'course'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPALM'"
op|':'
string|"'almanac'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPGRS'"
op|':'
string|"'range'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPGST'"
op|':'
string|"'noise'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPMSS'"
op|':'
string|"'beacon'"
op|','
comment|'# not implemented'
nl|'\n'
string|"'GPZDA'"
op|':'
string|"'time'"
op|','
comment|'# not implemented'
nl|'\n'
op|'}'
newline|'\n'
comment|'# generally you may miss the beginning of the first message'
nl|'\n'
DECL|variable|ignore_invalid_sentence
name|'ignore_invalid_sentence'
op|'='
number|'1'
newline|'\n'
comment|"# checksums shouldn't be invalid"
nl|'\n'
DECL|variable|ignore_checksum_mismatch
name|'ignore_checksum_mismatch'
op|'='
number|'0'
newline|'\n'
comment|'# ignore unknown sentence types'
nl|'\n'
DECL|variable|ignore_unknown_sentencetypes
name|'ignore_unknown_sentencetypes'
op|'='
number|'0'
newline|'\n'
comment|"# do we want to even bother checking to see if it's from the 20th century?"
nl|'\n'
DECL|variable|convert_dates_before_y2k
name|'convert_dates_before_y2k'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|lineReceived
name|'def'
name|'lineReceived'
op|'('
name|'self'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'$'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'ignore_invalid_sentence'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'raise'
name|'InvalidSentence'
op|'('
string|'"%r does not begin with $"'
op|'%'
op|'('
name|'line'
op|','
op|')'
op|')'
newline|'\n'
comment|'# message is everything between $ and *, checksum is xor of all ASCII values of the message'
nl|'\n'
dedent|''
name|'strmessage'
op|','
name|'checksum'
op|'='
name|'line'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|"'*'"
op|')'
newline|'\n'
name|'message'
op|'='
name|'strmessage'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'sentencetype'
op|','
name|'message'
op|'='
name|'message'
op|'['
number|'0'
op|']'
op|','
name|'message'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'dispatch'
op|'='
name|'self'
op|'.'
name|'dispatch'
op|'.'
name|'get'
op|'('
name|'sentencetype'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'dispatch'
op|')'
name|'and'
op|'('
name|'not'
name|'self'
op|'.'
name|'ignore_unknown_sentencetypes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidSentence'
op|'('
string|'"sentencetype %r"'
op|'%'
op|'('
name|'sentencetype'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'ignore_checksum_mismatch'
op|':'
newline|'\n'
indent|'            '
name|'checksum'
op|','
name|'calculated_checksum'
op|'='
name|'int'
op|'('
name|'checksum'
op|','
number|'16'
op|')'
op|','
name|'reduce'
op|'('
name|'operator'
op|'.'
name|'xor'
op|','
name|'map'
op|'('
name|'ord'
op|','
name|'strmessage'
op|')'
op|')'
newline|'\n'
name|'if'
name|'checksum'
op|'!='
name|'calculated_checksum'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'InvalidChecksum'
op|'('
string|'"Given 0x%02X != 0x%02X"'
op|'%'
op|'('
name|'checksum'
op|','
name|'calculated_checksum'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'handler'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|'"handle_%s"'
op|'%'
name|'dispatch'
op|','
name|'None'
op|')'
newline|'\n'
name|'decoder'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|'"decode_%s"'
op|'%'
name|'dispatch'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'dispatch'
name|'and'
name|'handler'
name|'and'
name|'decoder'
op|')'
op|':'
newline|'\n'
comment|'# missing dispatch, handler, or decoder'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|'# return handler(*decoder(*message))'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'decoded'
op|'='
name|'decoder'
op|'('
op|'*'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidSentence'
op|'('
string|'"%r is not a valid %s (%s) sentence"'
op|'%'
op|'('
name|'line'
op|','
name|'sentencetype'
op|','
name|'dispatch'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'handler'
op|'('
op|'*'
name|'decoded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|decode_position
dedent|''
name|'def'
name|'decode_position'
op|'('
name|'self'
op|','
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|','
name|'utc'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'latitude'
op|','
name|'longitude'
op|'='
name|'self'
op|'.'
name|'_decode_latlon'
op|'('
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|')'
newline|'\n'
name|'utc'
op|'='
name|'self'
op|'.'
name|'_decode_utc'
op|'('
name|'utc'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|"'A'"
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'return'
op|'('
nl|'\n'
name|'latitude'
op|','
nl|'\n'
name|'longitude'
op|','
nl|'\n'
name|'utc'
op|','
nl|'\n'
name|'status'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|decode_positiontime
dedent|''
name|'def'
name|'decode_positiontime'
op|'('
name|'self'
op|','
name|'utc'
op|','
name|'status'
op|','
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|','
name|'speed'
op|','
name|'course'
op|','
name|'utcdate'
op|','
name|'magvar'
op|','
name|'magdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utc'
op|'='
name|'self'
op|'.'
name|'_decode_utc'
op|'('
name|'utc'
op|')'
newline|'\n'
name|'latitude'
op|','
name|'longitude'
op|'='
name|'self'
op|'.'
name|'_decode_latlon'
op|'('
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|')'
newline|'\n'
name|'if'
name|'speed'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'speed'
op|'='
name|'float'
op|'('
name|'speed'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'speed'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'course'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'course'
op|'='
name|'float'
op|'('
name|'course'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'course'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'utcdate'
op|'='
number|'2000'
op|'+'
name|'int'
op|'('
name|'utcdate'
op|'['
number|'4'
op|':'
number|'6'
op|']'
op|')'
op|','
name|'int'
op|'('
name|'utcdate'
op|'['
number|'2'
op|':'
number|'4'
op|']'
op|')'
op|','
name|'int'
op|'('
name|'utcdate'
op|'['
number|'0'
op|':'
number|'2'
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'convert_dates_before_y2k'
name|'and'
name|'utcdate'
op|'['
number|'0'
op|']'
op|'>'
number|'2073'
op|':'
newline|'\n'
comment|'# GPS was invented by the US DoD in 1973, but NMEA uses 2 digit year.'
nl|'\n'
comment|"# Highly unlikely that we'll be using NMEA or this twisted module in 70 years,"
nl|'\n'
comment|"# but remotely possible that you'll be using it to play back data from the 20th century."
nl|'\n'
indent|'            '
name|'utcdate'
op|'='
op|'('
name|'utcdate'
op|'['
number|'0'
op|']'
op|'-'
number|'100'
op|','
name|'utcdate'
op|'['
number|'1'
op|']'
op|','
name|'utcdate'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'magvar'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'magvar'
op|'='
name|'float'
op|'('
name|'magvar'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'magdir'
op|'=='
string|"'W'"
op|':'
newline|'\n'
indent|'            '
name|'magvar'
op|'='
op|'-'
name|'magvar'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'magvar'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'('
nl|'\n'
name|'latitude'
op|','
nl|'\n'
name|'longitude'
op|','
nl|'\n'
name|'speed'
op|','
nl|'\n'
name|'course'
op|','
nl|'\n'
comment|'# UTC seconds past utcdate'
nl|'\n'
name|'utc'
op|','
nl|'\n'
comment|'# UTC (year, month, day)'
nl|'\n'
name|'utcdate'
op|','
nl|'\n'
comment|'# None or magnetic variation in degrees (west is negative)'
nl|'\n'
name|'magvar'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_decode_utc
dedent|''
name|'def'
name|'_decode_utc'
op|'('
name|'self'
op|','
name|'utc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utc_hh'
op|','
name|'utc_mm'
op|','
name|'utc_ss'
op|'='
name|'map'
op|'('
name|'float'
op|','
op|'('
name|'utc'
op|'['
op|':'
number|'2'
op|']'
op|','
name|'utc'
op|'['
number|'2'
op|':'
number|'4'
op|']'
op|','
name|'utc'
op|'['
number|'4'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'utc_hh'
op|'*'
number|'3600.0'
op|'+'
name|'utc_mm'
op|'*'
number|'60.0'
op|'+'
name|'utc_ss'
newline|'\n'
nl|'\n'
DECL|member|_decode_latlon
dedent|''
name|'def'
name|'_decode_latlon'
op|'('
name|'self'
op|','
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'latitude'
op|'='
name|'float'
op|'('
name|'latitude'
op|'['
op|':'
number|'2'
op|']'
op|')'
op|'+'
name|'float'
op|'('
name|'latitude'
op|'['
number|'2'
op|':'
op|']'
op|')'
op|'/'
number|'60.0'
newline|'\n'
name|'if'
name|'ns'
op|'=='
string|"'S'"
op|':'
newline|'\n'
indent|'            '
name|'latitude'
op|'='
op|'-'
name|'latitude'
newline|'\n'
dedent|''
name|'longitude'
op|'='
name|'float'
op|'('
name|'longitude'
op|'['
op|':'
number|'3'
op|']'
op|')'
op|'+'
name|'float'
op|'('
name|'longitude'
op|'['
number|'3'
op|':'
op|']'
op|')'
op|'/'
number|'60.0'
newline|'\n'
name|'if'
name|'ew'
op|'=='
string|"'W'"
op|':'
newline|'\n'
indent|'            '
name|'longitude'
op|'='
op|'-'
name|'longitude'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'latitude'
op|','
name|'longitude'
op|')'
newline|'\n'
nl|'\n'
DECL|member|decode_activesatellites
dedent|''
name|'def'
name|'decode_activesatellites'
op|'('
name|'self'
op|','
name|'mode1'
op|','
name|'mode2'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'satellites'
op|','
op|'('
name|'pdop'
op|','
name|'hdop'
op|','
name|'vdop'
op|')'
op|'='
name|'args'
op|'['
op|':'
number|'12'
op|']'
op|','
name|'map'
op|'('
name|'float'
op|','
name|'args'
op|'['
number|'12'
op|':'
op|']'
op|')'
newline|'\n'
name|'satlist'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'satellites'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'n'
op|':'
newline|'\n'
indent|'                '
name|'satlist'
op|'.'
name|'append'
op|'('
name|'int'
op|'('
name|'n'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'satlist'
op|'.'
name|'append'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'mode'
op|'='
op|'('
name|'mode1'
op|','
name|'int'
op|'('
name|'mode2'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
nl|'\n'
comment|'# satellite list by channel'
nl|'\n'
name|'tuple'
op|'('
name|'satlist'
op|')'
op|','
nl|'\n'
comment|'# (MODE_AUTO/MODE_FORCED, MODE_NOFIX/MODE_2DFIX/MODE_3DFIX)'
nl|'\n'
name|'mode'
op|','
nl|'\n'
comment|'# position dilution of precision'
nl|'\n'
name|'pdop'
op|','
nl|'\n'
comment|'# horizontal dilution of precision'
nl|'\n'
name|'hdop'
op|','
nl|'\n'
comment|'# vertical dilution of precision'
nl|'\n'
name|'vdop'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|decode_fix
dedent|''
name|'def'
name|'decode_fix'
op|'('
name|'self'
op|','
name|'utc'
op|','
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|','
name|'posfix'
op|','
name|'satellites'
op|','
name|'hdop'
op|','
name|'altitude'
op|','
name|'altitude_units'
op|','
name|'geoid_separation'
op|','
name|'geoid_separation_units'
op|','
name|'dgps_age'
op|','
name|'dgps_station_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'latitude'
op|','
name|'longitude'
op|'='
name|'self'
op|'.'
name|'_decode_latlon'
op|'('
name|'latitude'
op|','
name|'ns'
op|','
name|'longitude'
op|','
name|'ew'
op|')'
newline|'\n'
name|'utc'
op|'='
name|'self'
op|'.'
name|'_decode_utc'
op|'('
name|'utc'
op|')'
newline|'\n'
name|'posfix'
op|'='
name|'int'
op|'('
name|'posfix'
op|')'
newline|'\n'
name|'satellites'
op|'='
name|'int'
op|'('
name|'satellites'
op|')'
newline|'\n'
name|'hdop'
op|'='
name|'float'
op|'('
name|'hdop'
op|')'
newline|'\n'
name|'altitude'
op|'='
op|'('
name|'float'
op|'('
name|'altitude'
op|')'
op|','
name|'altitude_units'
op|')'
newline|'\n'
name|'if'
name|'geoid_separation'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'geoid'
op|'='
op|'('
name|'float'
op|'('
name|'geoid_separation'
op|')'
op|','
name|'geoid_separation_units'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'geoid'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'dgps_age'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'dgps'
op|'='
op|'('
name|'float'
op|'('
name|'dgps_age'
op|')'
op|','
name|'dgps_station_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'dgps'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'('
nl|'\n'
comment|'# seconds since 00:00 UTC'
nl|'\n'
name|'utc'
op|','
nl|'\n'
comment|'# latitude (degrees)'
nl|'\n'
name|'latitude'
op|','
nl|'\n'
comment|'# longitude (degrees)'
nl|'\n'
name|'longitude'
op|','
nl|'\n'
comment|'# position fix status (POSFIX_INVALID, POSFIX_SPS, POSFIX_DGPS, POSFIX_PPS)'
nl|'\n'
name|'posfix'
op|','
nl|'\n'
comment|'# number of satellites used for fix 0 <= satellites <= 12 '
nl|'\n'
name|'satellites'
op|','
nl|'\n'
comment|'# horizontal dilution of precision'
nl|'\n'
name|'hdop'
op|','
nl|'\n'
comment|"# None or (altitude according to WGS-84 ellipsoid, units (typically 'M' for meters)) "
nl|'\n'
name|'altitude'
op|','
nl|'\n'
comment|"# None or (geoid separation according to WGS-84 ellipsoid, units (typically 'M' for meters))"
nl|'\n'
name|'geoid'
op|','
nl|'\n'
comment|'# (age of dgps data in seconds, dgps station id)'
nl|'\n'
name|'dgps'
op|','
nl|'\n'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
