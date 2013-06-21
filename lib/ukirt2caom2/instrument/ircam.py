from caom2 import Instrument
from jcmt2caom2.raw import keywordvalue

from ukirt2caom2 import IngestionError
from ukirt2caom2.instrument import instrument_classes
from ukirt2caom2.instrument.ukirt import ObservationUKIRT
from ukirt2caom2.util import clean_header

class ObservationIRCAM(ObservationUKIRT):
    def ingest_instrument(self, headers):
        instrument = Instrument('ircam')

        self.caom2.instrument = instrument

    def get_spectral_wcs(self, headers):
        return None

    def get_spatial_wcs(self, headers, translated):
        return None

instrument_classes['ircam'] = ObservationIRCAM
