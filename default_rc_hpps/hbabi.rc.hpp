// Source: https://switchbrew.org/wiki/Homebrew_ABI#Loader_Config_Keys

R_DEFINE_NAMESPACE_RESULT_MODULE(hbabi, 346);

namespace hbabi {

    R_DEFINE_ERROR_RANGE(UnrecognizedEntryKey, 100, 199);
    R_DEFINE_ERROR_RANGE(MandatoryEntryNotPresent, 200, 299);
    R_DEFINE_ERROR_RANGE(InvalidEntryValidation, 300, 399);

}