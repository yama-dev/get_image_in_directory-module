#!/usr/bin/perl

# get_image_in_directory-module Perl Library v0.0.1
# https://github.com/yama-dev/get_image_in_directory-module
# Copyright yama-dev
# Licensed under the MIT license.
# Date: 2018-03-20
#
# 特定フォルダの最新画像を取得をして、json 形式で出力するスクリプト
# @return $json | srt (json)

use strict;
use utf8;
use warnings;

# Import Modules.
use JSON;
use CGI;
use POSIX 'strftime';

my @file = glob "images/*.jpg images/*.gif images/*.png";

my @list = ();
foreach my $filepath (@file) {
  my @filestat = stat $filepath;
  my $filestat_time = $filestat[9];
  my $filestat_time_str = strftime "%Y/%m/%d %H:%M:%S", localtime($filestat_time);
  my $filedate = {
    path => $filepath,
    time => $filestat_time,
    time_str => $filestat_time_str,
  };
  push(@list, ($filedate));
}

my $date_str = strftime "%Y/%m/%d %H:%M:%S", localtime;

# Sort File List.
my @list = sort{$b->{'time'} <=> $a->{'time'}} @list;

# Choice data.
my @listfix = @list[1..3];

# Set Data.
my $hash = {
  varsion => '0.0.1',
  date => $date_str,
  list => [ @listfix ]
};

# Encode.
my $json = JSON->new->utf8(0)->encode($hash);
  
# Output json.
print CGI::header(-type => 'application/json', -charset => 'UTF-8');
print $json;
