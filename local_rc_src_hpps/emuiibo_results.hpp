// Source: https://github.com/XorTroll/emuiibo/blob/master/emuiibo/src/rc.rs

R_DEFINE_NAMESPACE_RESULT_MODULE(emuiibo, 352);

namespace emuiibo {

    R_DEFINE_ERROR_RESULT(VirtualAmiiboFlagNotFound, 1);
    R_DEFINE_ERROR_RESULT(VirtualAmiiboJsonNotFound, 2);
    R_DEFINE_ERROR_RESULT(InvalidJsonSerialization, 3);
    R_DEFINE_ERROR_RESULT(InvalidJsonDeserialization, 4);
    R_DEFINE_ERROR_RESULT(InvalidLoadedVirtualAmiibo, 5);
    R_DEFINE_ERROR_RESULT(VirtualAmiiboAreasJsonNotFound, 6);
    R_DEFINE_ERROR_RESULT(InvalidActiveVirtualAmiibo, 7);
    R_DEFINE_ERROR_RESULT(InvalidVirtualAmiiboAccessId, 8);

}