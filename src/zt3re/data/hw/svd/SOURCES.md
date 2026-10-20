# Vendor inputs for tools/svd2hw.py

These files are unmodified copies (except the `*_irqn.h` extracts) of public upstream
material; they are kept here so `tools/svd2hw.py` is reproducible without network access.

| File | Upstream | Revision | Licence |
|------|----------|----------|---------|
| `AT32F415xx_v2.svd` | https://github.com/ArteryTek/AT32F415_Firmware_Library `utilities/at32f415_gen_random_number_demo/at32_ide/SVD/AT32F415xx_v2.svd` (identical copies exist in `project/at_start_f415/templates/at32_ide/SVD/`) | commit `773f88703eddd7b49d72d36ae560b887f67ee9fb` (2025-11-27), md5 `188872aca399e6435a446a12be621642` | BSD-3-Clause (ArteryTek, `LICENSE.ArteryTek-BSD-3-Clause`); the file carries ARM's BSD-style SVD header |
| `startup_at32f415.s` | same repo, `libraries/cmsis/cm4/device_support/startup/gcc/startup_at32f415.s` | same commit | BSD-3-Clause (ArteryTek) |
| `at32f415_irqn.h` | same repo, `IRQn_Type` enum of `libraries/cmsis/cm4/device_support/at32f415.h` | same commit | BSD-3-Clause (ArteryTek) |
| `STM32G0B1.svd` | https://github.com/modm-io/cmsis-svd-stm32 `stm32g0/STM32G0B1.svd` (ST's own SVD v1.8 as published by ST, line endings normalised by modm) | commit `e79021accd49bf19bd0b16065f5471fb073ff3ac`, md5 `febf12e570c1a5def2c7f453b9b30ba6` | Apache-2.0 (STMicroelectronics; header in the file, `LICENSE.STMicroelectronics-Apache-2.0`) |
| `startup_stm32g0b1xx.s` | https://github.com/STMicroelectronics/cmsis_device_g0 `Source/Templates/gcc/startup_stm32g0b1xx.s` | commit `7c77b7cbcee497dfbb5cc08f9562a80515e78013` | Apache-2.0 (STMicroelectronics) |
| `stm32g0b1_irqn.h` | same repo, `IRQn_Type` enum of `Include/stm32g0b1xx.h` | same commit | Apache-2.0 (STMicroelectronics) |

The Zt3 repository itself has no top-level `LICENSE` file; the licences above are all
permissive redistribution licences, and the original copyright/licence texts are retained.
