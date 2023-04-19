use strict;
use warnings;

use IO::Uncompress::Unzip qw($UnzipError);

my $zipFile = $ARGV[0];
my $searchTerm = $ARGV[1];
my @filePaths;
my $i = 0;

	my $u = IO::Uncompress::Unzip->new($zipFile) or die "Error: $UnzipError\n";

	my $status;
	
	for ($status = 1; $status > 0; $status = $u->nextStream(), $i++) 
	{
	    	my $header = $u->getHeaderInfo();
	    	#my $zippedFile = $header->{Name};
	    	$filePaths[$i] = $header->{Name};
	    	if ($filePaths[$i] =~ /\/$/) 
	    	{
			last if $status < 0;
			next;
		}
		

	}
	for($i = 0; $i < $#filePaths; $i++)
	{
		if (index(lc($filePaths[$i]), lc($searchTerm)) != -1) 
		{
    			print "$filePaths[$i] \n";
		}
	}
