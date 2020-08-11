"""
Notice: the code within `run` is just an example of what can be done.

Feel free to import what's needed, including third-party libraries or
other self-written modules.
"""

import apache_beam as beam

import transforms


def run(input_pcol, job_config):
    """REQUIRED: Main entrypoint in running a job's transform(s).

    Any Beam transforms that need to happen after a message is consumed
    from PubSub from an upstream job, and before publishing a message to
    a downstream job (if needed/configured).

    Args:
        input_pcol: A Beam PCollection returned from
            ``beam.io.ReadFromPubSub``.
        job_config (klio.KlioJobConfig): Job-related configuration as
            defined in ``klio-job.yaml``.
    Returns:
        A Beam PCollection that will be passed to ``beam.io.WriteToPubSub``.
    """
    output_pcol = input_pcol | beam.ParDo(transforms.HelloKlio())
    # <-- multiple Klio-based ParDo transforms are supported here -->
    return output_pcol
