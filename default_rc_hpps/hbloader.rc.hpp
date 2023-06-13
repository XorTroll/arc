// Source: https://switchbrew.org/wiki/Error_codes#Homebrew_Errors

R_DEFINE_NAMESPACE_RESULT_MODULE(hbloader, 347);

namespace hbloader {

    R_DEFINE_ERROR_RESULT(SmInitFailure, 1);
    R_DEFINE_ERROR_RESULT(FsInitFailure, 2);
    R_DEFINE_ERROR_RESULT(NroOpenFailure, 3);
    R_DEFINE_ERROR_RESULT(NroHeaderReadFailure, 4);
    R_DEFINE_ERROR_RESULT(InvalidNroMagic, 5);
    R_DEFINE_ERROR_RESULT(InvalidNroSegments, 6);
    R_DEFINE_ERROR_RESULT(NroReadFailure, 7);
    R_DEFINE_ERROR_RESULT(AllocateHeapFailure, 9);
    R_DEFINE_ERROR_RESULT(MapCodeMemoryFailure, 18);
    R_DEFINE_ERROR_RESULT(MapTextFailure, 19);
    R_DEFINE_ERROR_RESULT(MapRodataFailure, 20);
    R_DEFINE_ERROR_RESULT(MapDataBssFailure, 21);
    R_DEFINE_ERROR_RESULT(UnmapTextFailure, 24);
    R_DEFINE_ERROR_RESULT(UnmapRodataFailure, 25);
    R_DEFINE_ERROR_RESULT(UnmapDataBssFailure, 26);

}